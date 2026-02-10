from django.shortcuts import render
from Admin.models import *
from Guest.models import *
from User.models import *


# Create your views here.
def AdminReg(request):
    admindata=tbl_admin.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_contact=contact,admin_password=password)
        return render(request,'Admin/AdminReg.html',{'msg':"Admin Registered"})
    else:
        return render(request,'Admin/AdminReg.html',{'admindata':admindata})
    
#AdminReg edit
def editAdreg(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        editdata.admin_name=name
        editdata.admin_email=email
        editdata.admin_contact=contact
        editdata.save()
        return render(request,'Admin/AdminReg.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/AdminReg.html',{'editdata':editdata})
    
#AdminReg delete
def delAdreg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,'Admin/AdminReg.html',{'msg':"data deleted"})


#district views
def District(request):
    dis=tbl_district.objects.all()
    if request.method=='POST':
        district=request.POST.get('txt_district')
        
        districtcount=tbl_district.objects.filter(district_name=district).count()
        if districtcount>0:

            return render(request,'Admin/District.html',{'msg':"District Already Exists"})
        else:
            tbl_district.objects.create(district_name=district)
            return render(request,'Admin/District.html',{'msg':"District Added"})
    else:
        return render(request,'Admin/District.html',{'district':dis})
    
#district delete
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':"data deleted"})

#district edit
def editdis(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        district=request.POST.get('txt_district')
        editdata.district_name=district
        editdata.save()
        return render(request,'Admin/District.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/District.html',{'editdata':editdata})


def Propertytype(request):
    pro=tbl_propertytype.objects.all()
    if request.method== 'POST':
        Propertytype=request.POST.get('txt_Propertytype')
        tbl_propertytype.objects.create(propertytype_name=Propertytype)
        return render(request, 'Admin/Propertytype.html',{'msg' : "Property type Added "})
    else:
        return render(request, 'Admin/Propertytype.html',{'Propertytype':pro})
    

def delpropertytype(request,did):
    tbl_propertytype.objects.get(id=did).delete()
    return render(request,'Admin/Propertytype.html',{'msg':"data deleted"})



def editpropertytype(request,eid):
    editdata=tbl_propertytype.objects.get(id=eid)
    if request.method=='POST':
        Propertytype=request.POST.get('txt_Propertytype')
        editdata.propertytype_name=Propertytype
        editdata.save()
        return render(request,'Admin/Propertytype.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Propertytype.html',{'editdata':editdata})
    


#category 
def Category(request):
    cat=tbl_category.objects.all()
    if request.method=='POST':
        category=request.POST.get('txt_Category')
        tbl_category.objects.create(category_name=category)
        return render(request,'Admin/Category.html',{'msg':"Category Added"})
    else:
        return render(request,'Admin/Category.html',{'Category':cat})
    

#category delete
def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return render(request,'Admin/Category.html',{'msg':"data deleted"})

#category edit
def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        Category=request.POST.get('txt_Category')
        editdata.category_name=Category
        editdata.save()
        return render(request,'Admin/Category.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Category.html',{'editdata':editdata})
    
#place views
def Place(request):
    pla=tbl_Place.objects.all()
    districtData=tbl_district.objects.all()
    if request.method == 'POST':
        Place=request.POST.get('txt_Place')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_Place.objects.create(place_name=Place,district=district)
        
        return render(request,'Admin/Place.html',{'msg':"Place Added"})
    else:
        return render(request,'Admin/Place.html',{'districtData':districtData,'Place':pla})

#place delete
def delplace(request,did):
    tbl_Place.objects.get(id=did).delete()
    return render(request,'Admin/Place.html',{'msg':"data deleted"})

#place edit
def editplace(request,eid):
    editdata=tbl_Place.objects.get(id=eid)
    districtData=tbl_district.objects.all()
    if request.method=='POST':
        Place=request.POST.get('txt_Place')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.place_name=Place
        editdata.district =  district
        editdata.save()
        return render(request,'Admin/Place.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Place.html',{'editdata':editdata,'districtData':districtData})
    
#subcategory views
def Subcategory(request):
    sub=tbl_Subcategory.objects.all()
    categoryData=tbl_category.objects.all()
    if request.method == 'POST':
            Subcategory=request.POST.get('txt_Subcategory')
            category=tbl_category.objects.get(id=request.POST.get('sel_category'))
            tbl_Subcategory.objects.create(subcategory_name=Subcategory,category=category)
            return render(request,'Admin/Subcategory.html',{'msg':"Subcategory Added"})
    else:
            return render(request,'Admin/Subcategory.html',{'categoryData':categoryData,'Subcategory':sub})
        
#subcategory delete
def delsubcategory(request,did):
    tbl_Subcategory.objects.get(id=did).delete()
    return render(request,'Admin/Subcategory.html',{'msg':"data deleted"})


#subcategory edit
def editsubcat(request,eid):
    editdata= tbl_Subcategory.objects.get(id=eid)
    categoryData=tbl_category.objects.all()
    if request.method=='POST':
        Subcategory=request.POST.get('txt_Subcategory')
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.subcategory_name=Subcategory
        editdata.category = category
        editdata.save()
        return render(request,'Admin/Subcategory.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Subcategory.html',{'editdata':editdata,'categoryData':categoryData})
    


def HomePage(request):
    admindata=tbl_admin.objects.get(id=request.session['aid'])
    feedback=tbl_feedback.objects.all().order_by('-id')[:3]  
    user_count=tbl_user.objects.count()
    seller_count=tbl_seller.objects.count()
    renter_count=tbl_renter.objects.count()
    property_count=tbl_propertybuing.objects.filter(propertybuying_status=1).count() 
    property_count1=tbl_propertybooking.objects.filter(propertybooking_status=1).count()
    total_count=property_count + property_count1
    return render(request,'Admin/HomePage.html',{'property_count':total_count,'admindata':admindata,'feedback':feedback,
                                                 'user_count':user_count,'seller_count':seller_count,'renter_count':renter_count})




def Userlist(request):
    pending=tbl_user.objects.filter(user_status=0)
    accept=tbl_user.objects.filter(user_status=1)
    reject=tbl_user.objects.filter(user_status=2)
    return render(request,'Admin/Userlist.html',{'pending':pending,'acceptuser':accept,'rejectuser':reject})

def acceptuser(request,act):
    data=tbl_user.objects.get(id=act)
    data.user_status=1
    data.save()
    return render(request,'Admin/Userlist.html',{'msg':"Accepted"})


def rejectuser(request,rej):
    data=tbl_user.objects.get(id=rej)
    data.user_status=2
    data.save()
    return render(request,'Admin/Userlist.html',{'msg':"Rejected"})


def Sellerlist(request):
    pending=tbl_seller.objects.all()
    return render(request,'Admin/Sellerlist.html',{'sellerlist':pending})

def acceptseller(request,act):
    data=tbl_seller.objects.get(id=act)
    data.seller_status=1
    data.save()
    return render(request,'Admin/Sellerlist.html',{'msg':"Accepted"})

def rejectseller(request,rej):
    data=tbl_seller.objects.get(id=rej)
    data.seller_status=2
    data.save()
    return render(request,'Admin/Sellerlist.html',{'msg':"Rejected"})

def Renterlist(request):
    renterlist=tbl_renter.objects.all()
    return render(request,'Admin/Renterlist.html',{'renterlist':renterlist})

def acceptrenter(request,act):
    data=tbl_renter.objects.get(id=act)
    data.renter_status=1
    data.save()
    return render(request,'Admin/Renterlist.html',{'msg':"Accepted"})


def rejectrenter(request,rej):
    data=tbl_renter.objects.get(id=rej)
    data.renter_status=2
    data.save()
    return render(request,'Admin/Renterlist.html',{'msg':"Rejected"})



def Viewcomplaints(request):
    user=tbl_user.objects.all()
    complaint=tbl_complaint.objects.filter(user_id__in=user)
    seller=tbl_seller.objects.all()
    scomplaint=tbl_complaint.objects.filter(seller_id__in=seller)
    renter=tbl_renter.objects.all()
    rcomplaint=tbl_complaint.objects.filter(renter_id__in=renter)

    return render(request,'Admin/Viewcomplaints.html',{'complaint':complaint,'scomplaint':scomplaint,'rcomplaint':rcomplaint})



def Reply(request,rid):
    complaintData=tbl_complaint.objects.get(id=rid)
    if request.method=='POST':
        reply=request.POST.get('txt_Reply')
        complaintData.complaint_reply=reply
        complaintData.complaint_status=1
        complaintData.save()
        
        return render(request,'Admin/Viewcomplaints.html',{'msg':"Replied Successfully",'rid':rid})
    else:
        return render(request,'Admin/Reply.html')
    


def Viewfeedback(request):
    user=tbl_user.objects.all()
    feedback=tbl_feedback.objects.filter(user_id__in=user)
    seller=tbl_seller.objects.all()
    sfeedback=tbl_feedback.objects.filter(seller_id__in=seller)
    renter=tbl_renter.objects.all()
    rfeedback=tbl_feedback.objects.filter(renter_id__in=renter)
    return render(request, 'Admin/Viewfeedback.html',{'feedback':feedback,'sfeedback':sfeedback,'rfeedback':rfeedback})

def Addbhk(request):
    bhk=tbl_bhk.objects.all()
    propertytypeData=tbl_propertytype.objects.all()
    if request.method=='POST':
        Addbhk=request.POST.get('txt_bhkdetails')
        propertytype=tbl_propertytype.objects.get(id=request.POST.get('sel_propertytype'))
        tbl_bhk.objects.create(bhk_name=Addbhk,propertytype=propertytype)
        return render(request,'Admin/Addbhk.html',{'msg':"BHK Added"})
    else:    
        return render(request,'Admin/Addbhk.html',{'propertytypeData':propertytypeData,'Addbhk':bhk})



def deladdbhk(request,did):
    tbl_bhk.objects.get(id=did).delete()
    return render(request,'Admin/Addbhk.html',{'msg':"data deleted"})


def editaddbhk(request,eid):
    editdata= tbl_bhk.objects.get(id=eid)
    propertytypeData=tbl_propertytype.objects.all()
    if request.method=='POST':
        Addbhk=request.POST.get('txt_bhkdetails')
        Propertytype=tbl_propertytype.objects.get(id=request.POST.get('sel_propertytype'))
        editdata.bhk_name=Addbhk
        editdata.propertytype = Propertytype
        editdata.save()
        return render(request,'Admin/Addbhk.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Addbhk.html',{'editdata':editdata,'propertytypeData':propertytypeData})
    
def Furnish(request):
    furnish=tbl_furnish.objects.all()
    propertytypeData=tbl_propertytype.objects.all()
    if request.method=='POST':
        Furnish=request.POST.get('txt_furnishdetails')
        propertytype=tbl_propertytype.objects.get(id=request.POST.get('sel_propertytype'))
        tbl_furnish.objects.create(furnish_name=Furnish,propertytype=propertytype)
        return render(request,'Admin/Furnish.html',{'msg':"Furnisher Added"})
    else:    
        return render(request,'Admin/Furnish.html',{'propertytypeData':propertytypeData,'Furnish':furnish})
    

def delfurnish(request,did):
    tbl_furnish.objects.get(id=did).delete()
    return render(request,'Admin/Furnish.html',{'msg':"data deleted"})


def editfurnish(request,eid):
    editdata= tbl_furnish.objects.get(id=eid)
    propertytypeData=tbl_propertytype.objects.all()
    if request.method=='POST':
        Furnish=request.POST.get('txt_furnishdetails')
        Propertytype=tbl_propertytype.objects.get(id=request.POST.get('sel_propertytype'))
        editdata.furnish_name=Furnish
        editdata.propertytype = Propertytype
        editdata.save()
        return render(request,'Admin/Furnish.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Furnish.html',{'editdata':editdata,'propertytypeData':propertytypeData})