from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *


# Create your views here.
def UserReg(request):
    districtData=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        place=request.POST.get('sel_place')  
        photo=request.FILES.get('txt_photo')  
        password=request.POST.get('txt_password')    
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,
                                place=tbl_Place.objects.get(id=place),user_photo=photo,user_password=password)
        return render(request,'Guest/UserReg.html',{'msg':"User Registered"})
    else:
        return render(request,'Guest/UserReg.html',{'districtData':districtData})
    
def Login(request):
    if request.method=='POST':
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
        rentercount=tbl_renter.objects.filter(renter_email=email,renter_password=password).count()
        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('User:Home')
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:HomePage')
        elif sellercount>0:
            sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
            if sellerdata.seller_status== 0:
                return render(request,'Guest/Login.html',{'msg':"registraction pending"})
            elif sellerdata.seller_status== 2:
                return render(request,'Guest/Login.html',{'msg':"registraction rejected"})
            else:
                request.session['sid']=sellerdata.id
                return redirect('Seller:Home')
        elif rentercount>0:
            renterdata=tbl_renter.objects.get(renter_email=email,renter_password=password)
            if renterdata.renter_status== 0:
                return render(request,'Guest/Login.html',{'msg':"registraction pending"})
            elif renterdata.renter_status== 2:
                return render(request,'Guest/Login.html',{'msg':"registraction rejected"})
            else:
                request.session['rid']=renterdata.id
                return redirect('Renter:Home')
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email or Password"})
    else:
        return render(request,'Guest/Login.html')    
        

def Ajaxplace(request):
    did=request.GET.get('did')
    placeData=tbl_Place.objects.filter(district=did)
    return render(request,'Guest/AjaxPlace.html',{'placeData':placeData})

def Seller(request):
    districtData=tbl_district.objects.all()
    if request.method== 'POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        place=request.POST.get('sel_place')  
        photo=request.FILES.get('txt_photo')  
        proof=request.FILES.get('txt_proof')
        password=request.POST.get('txt_password')
        tbl_seller.objects.create(seller_name=name,seller_email=email,seller_contact=contact,seller_address=address,
                                  place=tbl_Place.objects.get(id=place),seller_photo=photo,seller_proof=proof,seller_password=password) 
        return render(request,'Guest/Seller.html',{'msg':"seller Registered"})
    else:
        return render(request,'Guest/Seller.html',{'districtData':districtData})
    
    
    
def Renterreg(request):
    districtData=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        place=request.POST.get('sel_place')  
        photo=request.FILES.get('txt_photo')  
        proof=request.FILES.get('txt_proof')
        password=request.POST.get('txt_password')
        tbl_renter.objects.create(renter_name=name,renter_email=email,renter_contact=contact,renter_address=address,
                                  place=tbl_Place.objects.get(id=place),renter_photo=photo,renter_proof=proof,renter_password=password)         
        
        return render(request,'Guest/Renterreg.html',{'msg':"Renter Registered"})
    else:
        return render(request,'Guest/Renterreg.html',{'districtData':districtData})
    

def Home(request):
    return render(request,'Guest/Home.html')