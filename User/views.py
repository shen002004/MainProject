from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Guest.models import *
from Seller.models import *
from User.chatbot import *
from User.models import*
from datetime import datetime, timedelta
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime


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
    placedata=tbl_Place.objects.all()
    districtdata=tbl_district.objects.all()
    properdata=tbl_property.objects.filter(property_status = 0)

    propertytypedata=tbl_propertytype.objects.all()
    bhkdata=tbl_bhk.objects.all()
    furnishdata=tbl_furnish.objects.all()
    return render(request,'User/Viewpro.html',{'properdata':properdata,'propertytypedata':propertytypedata,
                                               'bhkdata':bhkdata,'furnishdata':furnishdata,'placedata':placedata,'districtdata':districtdata})



def Ajaxplace(request):
    disid = request.GET.get('disid')
    placedata = tbl_Place.objects.filter(district=disid)
    return render(request, 'User/AjaxPlace.html', {'placedata': placedata})

def Ajaxpro(request):

    ptypeid = request.GET.get('did')
    bhk = request.GET.get('bhk')
    fid = request.GET.get('fid')
    print(fid)
    category = request.GET.get('category')
    disid = request.GET.get('disid')
    place = request.GET.get('pid')

    properdata = tbl_property.objects.filter(property_status__in=[0,1])

    if disid:
        properdata = properdata.filter(place_id__district_id=disid)

    if place:
        properdata = properdata.filter(place_id=place)

    if ptypeid:
        properdata = properdata.filter(propertytype_id=ptypeid)

    if bhk:
        properdata = properdata.filter(bhk_id=bhk)

    if fid:
        properdata = properdata.filter(furnish_id=fid)

    if category and category != "ALL":
        properdata = properdata.filter(category_id__category_name=category)
    
    return render(request,'User/Ajaxpro.html',{'properdata': properdata})






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
    return render(request,'User/ViewGallery.html',{'data':data,'id':pid})


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
        bookingdata = tbl_propertybookingpayment.objects.get(id=bid,propertybookingpayment_status=0)
        if request.method=='POST':
            bookingdata.propertybookingpayment_status=1
            bookingdata.save()
            return redirect("User:loader")
        else:
            return render(request,'User/AddPayment.html',{"amount":bookingdata.propertybookingpayment_amount})
        
def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Paymentsuc.html")


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
    
def Proviewmore(request,id):

    properdata=tbl_property.objects.get(id=id)
    bhkdata=tbl_bhk.objects.all()
    furnish=tbl_furnish.objects.all()

    return render(request,'User/Proviewmore.html',{'properdata':properdata,'bhkdata':bhkdata,'furnish':furnish})

# def chatbot_api(request):
#     user_message = request.GET.get("user_input")
#     if not user_message:
#         return JsonResponse({"reply": "Please type something."})

#     response = predict_response(user_message)
#     return JsonResponse({"reply": response})

def chatbot_api(request):
    user_message = request.GET.get("text", "")

    if user_message == "":
        return JsonResponse({"reply": "Please type something"})

    response = predict_response(user_message)

    return JsonResponse({"reply": response})    




def viewauctionlist(request):
    # gallery=tbl_gallery.objects.all()
    auction = tbl_auctionhead.objects.filter(auctionhead_status__in=[0,1])
    # print(time(0, 0, 30))
    return render(request,"User/ViewAuctionList.html",{"auction":auction})

def auction(request, id):
    auction = tbl_auctionhead.objects.get(id=id)
    return render(request,"User/Auction.html",{"auction":auction,"id":id})

def ajaxplacebid(request):
    # print(request.GET.get("amount"))
    if int(request.GET.get("amount")) > int(request.GET.get("amt")):
        getamount = tbl_auctionbody.objects.filter(auction=request.GET.get("auctionid")).last()
        if getamount:
            if int(getamount.auctionbody_amount) < int(request.GET.get("amount")):
                tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
                timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
                if timer > 0:
                    t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                    t.timmer = time(0, 0, 30)  # Adds 30 seconds
                    t.save()
                else:
                    tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
                return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
            else:
                return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})
        else:
            tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
            timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
            if timer > 0:
                t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                t.timmer = time(0, 0, 30)  # Adds 30 seconds
                t.save()
            else:
                tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
            return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
    else:
        return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})

def ajaxgetbid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    if auctiondata:
        return JsonResponse({"user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})
    else:
        return JsonResponse({"user":"","amount":0})

def ajaxclosebid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    # print(auctiondata.id)
    auctionbody = tbl_auctionbody.objects.get(id=auctiondata.id)
    auctionbody.auctionbody_status = 1
    auctionbody.save()
    auctionhead = tbl_auctionhead.objects.get(id=auctiondata.auction.id)
    auctionhead.auctionhead_status = 2 
    auctionhead.auction_totalamount = auctionbody.auctionbody_amount
    auctionhead.save()
    # time = tbl_timmer.objects.get(auction=auctionid)
    # time.timmer_status = 1
    # time.save()
    return JsonResponse({"msg":"Auction Completed...","user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})

def ajaxgettimmer(request):
    auction_id = request.GET.get("auctionid")
    userdata = tbl_auctionbody.objects.filter(auction=auction_id).last()

    if userdata is not None:
        userid = userdata.user.id
        if userid == request.session["uid"]:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id, timmer_status=0).count()
            if timmer_count > 0:
                t = tbl_timmer.objects.get(auction=auction_id)
                if t.timmer > time(0, 0, 0):
                    # Convert time to datetime for subtraction
                    current_time = datetime.combine(datetime.today(), t.timmer)
                    new_time = (current_time - timedelta(seconds=1)).time()

                    # Update timer in database
                    t.timmer = new_time
                    t.save()

                    return JsonResponse({"time": t.timmer, "time_up": False})
                else:   
                    # Timer expired
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
        else:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id).count()
            if timmer_count > 0:
                ti = tbl_timmer.objects.filter(auction=auction_id).last()
                if ti.timmer > time(0, 0, 0):
                    return JsonResponse({"time": ti.timmer, "time_up": False})
                else:
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
    else:
        return JsonResponse({"time": time(0, 0, 30), "time_up": False})

def myauction(request):
    auction = tbl_auctionbody.objects.filter(user=request.session["uid"],auctionbody_status=1)
    return render(request,"User/MyAuction.html",{'auction':auction})

def auctionpayment(request, id):
    auction = tbl_auctionbody.objects.get(id=id)
    amount = auction.auctionbody_amount
    auc = tbl_auctionhead.objects.get(id=auction.auction.id)
    if request.method == "POST":
        artwork = tbl_property.objects.get(id=auc.property.id)
        artwork.property_status=3
        artwork.save()
        auc.auctionhead_status = 3
        auc.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amount})
