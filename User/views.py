from urllib import request
from django.shortcuts import render, redirect
from Guest.models import *
from Seller.models import *
from User.models import*
from datetime import datetime, timedelta


# Create your views here.
def Home(request):
    return render(request,'User/Home.html')

def Myprofile(request):
    uid = request.session.get('uid')
    if not uid:
        return redirect('Guest:Login')
    try:
        userdata = tbl_user.objects.get(id=uid)
    except tbl_user.DoesNotExist:
        return redirect('Guest:Login')
    return render(request,'User/Myprofile.html',{'userdata':userdata})


def Editprofile(request):
    uid = request.session.get('uid')
    if not uid:
        return redirect('Guest:Login')
    try:
        userdata = tbl_user.objects.get(id=uid)
    except tbl_user.DoesNotExist:
        return redirect('Guest:Login')
    if request.method=='POST':
        userdata.user_name=request.POST.get('txt_username')
        userdata.user_email=request.POST.get('txt_email')
        userdata.user_contact=request.POST.get('txt_contact')
        userdata.user_address=request.POST.get('txt_address')
        userdata.save()
        return render(request,'User/Editprofile.html',{'msg':"Profile Updated"})    
    else:
        return render(request,'User/Editprofile.html',{'userdata':userdata})
    
def Changepas(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    userpass=userdata.user_password
    if request.method=='POST':
        oldpass=request.POST.get('txt_oldpassword')
        newpass=request.POST.get('txt_newpassword')
        confirmpass=request.POST.get('txt_confirmpass')
        if userpass==oldpass:
            if newpass==confirmpass:  
                userdata.user_password=request.POST.get('txt_newpassword')
                userdata.save()
            else:
                return render(request,'User/Changepas.html',{'msg':"New Password and Confirm Password are not matching"})
        else:
            return render(request,'User/Changepas.html',{'msg':"Old Password is incorrect"})
    else:    
        return render(request,'User/Changepas.html')
    
    return render(request,'User/Changepas.html',{'msg':"Password Changed Successfully"})

def Viewpro(request):
    properdata=tbl_property.objects.all()
    propertytypedata=tbl_propertytype.objects.all()
    return render(request,'User/Viewpro.html',{'properdata':properdata,'propertytypedata':propertytypedata})

def Ajaxpro(request):
    ptypeid=request.GET.get('did')
    properdata=tbl_property.objects.filter(propertytype_id=ptypeid)
    return render(request,'User/Ajaxpro.html',{'properdata':properdata})

def Buy(request,pid):
    buying=tbl_property.objects.get(id=pid)
    userdata = tbl_user.objects.get(id=request.session['uid'])
    buycount=tbl_propertybuing.objects.filter(user_id=userdata,property_id=buying).count()
    if buycount>0:
        return render(request, 'User/Viewpro.html',{'msg':"property already purchased"})
    else:
        tbl_propertybuing.objects.create(property_id=buying,user_id=userdata,propertybuying_amount=buying.property_price)
        return render(request, 'User/Viewpro.html',{'msg':"property purchased successfully"})
    


def ViewGallery(request,pid):
    data=tbl_gallery.objects.filter(property=pid)
    return render(request,'User/ViewGallery.html',{'data':data})


def PropertyRent(request, pid):
    ppt = tbl_property.objects.get(id=pid)
    userdata = tbl_user.objects.get(id=request.session['uid'])

    bookingCount = tbl_propertybooking.objects.filter(
        user_id=userdata,
        property_id=ppt
    ).count()

    if bookingCount > 0:
        return render(request, 'User/PropertyRent.html', {
            'msg': "Already Rented this property"
        })

    if request.method == 'POST':
        fromdate = datetime.strptime(
            request.POST.get('txt_fromdate'), '%Y-%m-%d'
        ).date()
        todate = datetime.strptime(
            request.POST.get('txt_todate'), '%Y-%m-%d'
        ).date()
        days = int(request.POST.get('txt_days'))

        monthly_price = int(ppt.property_price)
        daily_price = monthly_price // 30

        # 🔹 1. Create SINGLE property booking
        booking = tbl_propertybooking.objects.create(
            propertybooking_fromdate=fromdate,
            propertybooking_todate=todate,
            propertybooking_amount=(
                (days // 30) * monthly_price +
                (days % 30) * daily_price
            ),
            property_id=ppt,
            user_id=userdata
        )

        # 🔹 2. Create MULTIPLE payment records
        remaining_days = days
        payment_date = fromdate

        while remaining_days > 30:
            tbl_propertybookingpayment.objects.create(
                propertybookingpayment_amount=monthly_price,
                propertybooking_id=booking
            )
            remaining_days -= 30
            payment_date += timedelta(days=30)

        # 🔹 Remaining days payment
        if remaining_days > 0:
            amount = remaining_days * daily_price
            tbl_propertybookingpayment.objects.create(
                propertybookingpayment_amount=amount,
                propertybooking_id=booking
            )

        return render(request, 'User/PropertyRent.html', {
            'msg': "Booked Successfully"
        })

    return render(request, 'User/PropertyRent.html', {'ppt': ppt})

def Myprobooking(request):
    booking=tbl_propertybuing.objects.filter(user_id=request.session['uid'])
    return render(request,'User/Myprobooking.html',{'booking':booking})

def delbuy(request,did):
    tbl_propertybuing.objects.get(id=did).delete()
    return render(request,'User/Myprobooking.html',{'msg':"Booking deleted"})
    

def MyproRent(request):
    renting=tbl_propertybooking.objects.filter(user_id=request.session['uid'])
    return render(request,'User/MyproRent.html',{'renting':renting})


def delrent(request,did):
    tbl_propertybooking.objects.get(id=did).delete()
    return render(request,'User/MyproRent.html',{'msg':"Rent deleted"})


def AddPayment(request,bid):
    payData=tbl_propertybookingpayment.objects.filter(id=bid,propertybookingpayment_status=1).count()
    if payData>0:
        msg = "Already Rented this property"
        return render(request, 'User/Paymenthistory.html', {'msg': msg})
    else:
        if request.method=='POST':
            bookingdata = tbl_propertybookingpayment.objects.get(id=bid,propertybookingpayment_status=0)
            bookingdata.propertybookingpayment_status=1
            bookingdata.save()

            return render(request,'User/AddPayment.html',{'msg':"Payment Added"})
        else:
            return render(request,'User/AddPayment.html')


def Paymenthistory(request,bid):
        paydata=tbl_propertybooking.objects.get(id=bid)
        if paydata.propertybooking_status == 1:
            paymenthistory=tbl_propertybookingpayment.objects.filter(propertybooking_id=paydata)
            return render(request,'User/Paymenthistory.html',{'Payhistory':paymenthistory})
        else:
            msg = "Your booking is not yet accepted by renter"
            return render(request,'User/Paymenthistory.html',{'msg':msg,'bid':bid})      
        

def Complaint(request):
    com=tbl_complaint.objects.all()
    if request.method=='POST':
        title = request.POST.get('txt_title')
        content = request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,
                                     user_id=tbl_user.objects.get(id=request.session['uid']))
        return render(request,'User/Complaint.html',{'msg':"Complaint submited Successfully"})
    else:
        return render(request,'User/Complaint.html',{'complaint':com})

def delcom(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request, 'User/Complaint.html',{'msg':"Complaint deleted"})

def Feedback(request):
    if request.method=='POST':
        content = request.POST.get('txt_content')
        tbl_feedback.objects.create(feedback_content=content,
                                     user_id=tbl_user.objects.get(id=request.session['uid']))    
        return render(request,'User/Feedback.html',{'msg': "Feedback submited Successfully"})
    else:
        return render(request,'User/Feedback.html')




