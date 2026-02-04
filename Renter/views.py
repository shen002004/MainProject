from django.shortcuts import render
from Renter.models import *
from Guest.models import *
from Seller.models import *
from User.models import *


# Create your views here.
def Home(request):
    return render(request,'Renter/Home.html')

def Myprofile(request):
    renterdata=tbl_renter.objects.get(id=request.session['rid'])
    return render(request,'Renter/Myprofile.html',{'renterdata':renterdata})



def Editprofile(request):
    renterdata=tbl_renter.objects.get(id=request.session['rid'])
    if request.method=='POST':
        renterdata.renter_name=request.POST.get('txt_rentername')
        renterdata.renter_email=request.POST.get('txt_email')
        renterdata.renter_contact=request.POST.get('txt_contact')
        renterdata.renter_address=request.POST.get('txt_address')
        renterdata.save()
        return render(request,'Renter/Editprofile.html',{'msg':"Profile Updated"})    
    else:
        return render(request,'Renter/Editprofile.html',{'renterdata':renterdata})
    

    
    
def Changepas(request):
    renterdata=tbl_renter.objects.get(id=request.session['rid'])
    renterpass=renterdata.renter_password
    if request.method=='POST':
        oldpass=request.POST.get('txt_oldpassword')
        newpass=request.POST.get('txt_newpassword')
        confirmpass=request.POST.get('txt_confirmpass')
        if renterpass==oldpass:
            if newpass==confirmpass:  
                renterdata.renter_password=request.POST.get('txt_newpassword')
                renterdata.save()
            else:
                return render(request,'Renter/Changepas.html',{'msg':"New Password and Confirm Password are not matching"})
        else:
            return render(request,'Renter/Changepas.html',{'msg':"Old Password is incorrect"})
    else:    
        return render(request,'Renter/Changepas.html')
 
    return render(request,'Renter/Changepas.html',{'msg':"Password Changed Successfully"})   



def Addproperty(request):
    place=tbl_Place.objects.all()
    adp=tbl_property.objects.filter(renter_id=request.session['rid'])
    districtData=tbl_district.objects.all()
    propertytypedata=tbl_propertytype.objects.all()
    categorydata=tbl_category.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        description=request.POST.get('txt_description')
        propertytype=request.POST.get('sel_propertytype')
        photo=request.FILES.get('txt_photo')
        place=request.POST.get('sel_place')
        category=request.POST.get('sel_category')
        price=request.POST.get('txt_price')
        tbl_property.objects.create(property_name=name,property_description=description,property_photo=photo,
                                    propertytype_id=tbl_propertytype.objects.get(id=propertytype),
                    place_id=tbl_Place.objects.get(id=place),category_id=tbl_category.objects.get(id=category),
                    property_price=price,property_typestatus=0,renter_id=tbl_renter.objects.get(id=request.session['rid']))
        return render(request,'Renter/Addproperty.html',{'msg':"Property Added"})
    else:
        return render(request,'Renter/Addproperty.html',{'districtData':districtData,'categorydata':categorydata,'Addproperty':adp,'propertytypedata':propertytypedata})


def delpro(request,did):
    tbl_property.objects.get(id=did).delete()
    return render(request,'Renter/Addproperty.html',{'msg':"data deleted"})


def Gallery(request,pid):
    gal=tbl_property.objects.get(id=pid)
    gallery=tbl_gallery.objects.filter(property=pid)
    if request.method=='POST':
        gallery=request.FILES.get('txt_photo')
        tbl_gallery.objects.create(gallery_photo=gallery,property=gal)
        return render(request,'Renter/Gallery.html',{'msg':"photo Added","id":pid})
    else:
        return render(request,'Renter/Gallery.html',{'Gallery':gallery,"id":pid})

    
def delgal(request,did,id):
    tbl_gallery.objects.get(id=did).delete()
    return render(request,'Renter/Gallery.html',{'msg':"data deleted","id":id})



def Viewbookings(request):
    bookings=tbl_propertybooking.objects.filter(property_id__renter_id=request.session['rid'])
    return render(request,'Renter/Viewbooking.html',{'bookings':bookings})

def acceptpro(request,act):
    data=tbl_propertybooking.objects.get(id=act)
    data.propertybooking_status=1
    data.save()
    return render(request,'Renter/Addproperty.html',{'msg':"Accepted"})

def rejectpro(request,rej):
    data=tbl_propertybooking.objects.get(id=rej)
    data.propertybooking_status=2
    data.save()
    return render(request,'Renter/Addproperty.html',{'msg':"Rejected"})


def Complaint(request):
    com=tbl_complaint.objects.filter(renter_id=request.session['rid'])
    if request.method=='POST':
        title = request.POST.get('txt_title')
        content = request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,
                                     renter_id=tbl_renter.objects.get(id=request.session['rid']))
        return render(request,'Renter/Complaint.html',{'msg':"Complaint submited Successfully"})
    else:
        return render(request,'Renter/Complaint.html',{'complaint':com})
    
    
def delcom(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request, 'Renter/Complaint.html',{'msg':"Complaint deleted"})


def Feedback(request):
    if request.method=='POST':
        content = request.POST.get('txt_content')
        tbl_feedback.objects.create(feedback_content=content,
                                     renter_id=tbl_renter.objects.get(id=request.session['rid']))    
        return render(request,'Renter/Feedback.html',{'msg': "Feedback submited Successfully"})
    else:
        return render(request,'Renter/Feedback.html')
    





    
    
    