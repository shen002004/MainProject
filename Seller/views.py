from django.shortcuts import render
from Guest.models import *
from Seller.models import *
from User.models import *

# Create your views here.

def Myprofile(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,'Seller/Myprofile.html',{'sellerdata':sellerdata})

def Editprofile(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=='POST':
        sellerdata.seller_name=request.POST.get('txt_sellername')
        sellerdata.seller_email=request.POST.get('txt_email')
        sellerdata.seller_contact=request.POST.get('txt_contact')
        sellerdata.seller_address=request.POST.get('txt_address')
        sellerdata.save()
        return render(request,'Seller/Editprofile.html',{'msg':"Profile Updated"})    
    else:
        return render(request,'Seller/Editprofile.html',{'sellerdata':sellerdata})
    
    
def Changepas(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    sellerpass=sellerdata.seller_password
    if request.method=='POST':
        oldpass=request.POST.get('txt_oldpassword')
        newpass=request.POST.get('txt_newpassword')
        confirmpass=request.POST.get('txt_confirmpass')
        if sellerpass==oldpass:
            if newpass==confirmpass:  
                sellerdata.seller_password=request.POST.get('txt_newpassword')
                sellerdata.save()
            else:
                return render(request,'Seller/Changepas.html',{'msg':"New Password and Confirm Password are not matching"})
        else:
            return render(request,'Seller/Changepas.html',{'msg':"Old Password is incorrect"})
    else:    
        return render(request,'Seller/Changepas.html')
    
    return render(request,'Seller/Changepas.html',{'msg':"Password Changed Successfully"})    
    
    
def Home(request):
    return render(request,'Seller/Home.html')


def Addproperty(request):
    place=tbl_Place.objects.all()
    adp=tbl_property.objects.filter(seller_id=request.session['sid'])
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
                    place_id=tbl_Place.objects.get(id=place),category_id=tbl_category.objects.get(id=category),property_price=price,
                    property_typestatus=1,seller_id=tbl_seller.objects.get(id=request.session['sid']))
        return render(request,'Seller/Addproperty.html',{'msg':"Property Added"})   
    else:
        return render(request,'Seller/Addproperty.html',{'districtData':districtData,'categorydata':categorydata,'Addproperty':adp,'propertytypedata':propertytypedata})
    
def delpro(request,did):
    tbl_property.objects.get(id=did).delete()
    return render(request,'Seller/Addproperty.html',{'msg':"data deleted"})



def Gallery(request,pid):
    gal=tbl_property.objects.get(id=pid)
    gallery=tbl_gallery.objects.filter(property=pid)
    if request.method=='POST':
     gallery=request.FILES.get('txt_photo')
     tbl_gallery.objects.create(gallery_photo=gallery,property=gal)
     return render(request,'Seller/Gallery.html',{'msg':"photo Added","id":pid})
    else:
     return render(request,'Seller/Gallery.html',{'Gallery':gallery,"id":pid})
 
 
def delgal(request,did,id):
    tbl_gallery.objects.get(id=did).delete()
    return render(request,'Seller/Gallery.html',{'msg':"data deleted","id":id})



def Complaint(request):
    com=tbl_complaint.objects.filter(seller_id=request.session['sid'])
    if request.method=='POST':
        title = request.POST.get('txt_title')
        content = request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,
                                     seller_id=tbl_seller.objects.get(id=request.session['sid']))
        return render(request,'Seller/Complaint.html',{'msg':"Complaint submited Successfully"})
    else:
        return render(request,'Seller/Complaint.html',{'complaint':com})
    

def delcom(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request, 'Seller/Complaint.html',{'msg':"Complaint deleted"})

def Feedback(request):
    if request.method=='POST':
        content = request.POST.get('txt_content')
        tbl_feedback.objects.create(feedback_content=content,
                                     seller_id=tbl_seller.objects.get(id=request.session['sid']))    
        return render(request,'Seller/Feedback.html',{'msg': "Feedback submited Successfully"})
    else:
        return render(request,'Seller/Feedback.html')
    

def Viewbooking(request):
    sbooking=tbl_propertybuing.objects.filter(property_id__seller_id=request.session['sid'])
    return render(request,'Seller/Viewbooking.html',{'sbooking':sbooking})

def acceptbuying(request,act):
    data=tbl_propertybuing.objects.get(id=act)
    data.propertybuying_status=1
    data.save()
    return render(request,'Seller/Viewbooking.html',{'msg':"Accepted"})

def rejectbuying(request,rej):
    data=tbl_propertybuing.objects.get(id=rej)
    data.propertybuying_status=2
    data.save()
    return render(request,'Seller/Viewbooking.html',{'msg':"Rejected"})

def Ajaxbf(request):
    bhkcount = tbl_bhk.objects.filter(propertytype_id=request.GET.get('did')).count()
    funcount = tbl_furnish.objects.filter(propertytype_id=request.GET.get('did')).count()
    if bhkcount and funcount > 0:
        bhk = tbl_bhk.objects.filter(propertytype_id=request.GET.get('did'))
        fun = tbl_furnish.objects.filter(propertytype_id=request.GET.get('did'))
        return render(request,'Seller/Ajaxbf.html',{'bhk':bhk,'fun':fun})