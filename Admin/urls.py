
from django.urls import path
from Admin import views
app_name='Admin'

urlpatterns = [
    path('AdminReg/',views.AdminReg,name='AdminReg'),
    path('editAdreg/<int:eid>/',views.editAdreg,name='editAdreg'),
    path('delAdreg/<int:did>',views.delAdreg,name='delAdreg'),

    
    path('District/',views.District,name='District'),
    path('deldistrict/<int:did>',views.deldistrict,name='deldistrict'),
    path('editdis/<int:eid>/',views.editdis,name='editdis'),
    
    path('Category/',views.Category,name='Category'),
    path('delcategory/<int:did>',views.delcategory,name='delcategory'),
    path('editcategory/<int:eid>/',views.editcategory,name='editcategory'),
        
    path('Place/',views.Place,name='Place'),
    path('delplace/<int:did>',views.delplace,name='delplace'),
    path('editplace/<int:eid>/',views.editplace,name='editplace'),
    
    path('Subcategory/',views.Subcategory,name='Subcategory'),
    path('delsubcategory/<int:did>/',views.delsubcategory,name='delsubcategory'),
    path('editsubcat/<int:eid>/',views.editsubcat,name='editsubcat'),
    
    path('HomePage/',views.HomePage,name='HomePage'),
    
    path('Userlist/',views.Userlist,name='Userlist'),
    path('acceptuser/<int:act>',views.acceptuser,name='acceptuser'),
    path('rejectuser/<int:rej>',views.rejectuser,name='rejectuser'),
   
    path('Sellerlist/',views.Sellerlist,name='Sellerlist'),
    path('acceptseller/<int:act>',views.acceptseller,name='acceptseller'),
    path('rejectseller/<int:rej>',views.rejectseller,name='rejectseller'),
    
    path('Renterlist/',views.Renterlist,name='Renterlist'),
    path('acceptrenter/<int:act>',views.acceptrenter,name='acceptrenter'),
    path('rejectrenter/<int:rej>',views.rejectrenter,name='rejectrenter'),    

    path('Viewcomplaints/',views.Viewcomplaints,name='Viewcomplaints'),

    path('Reply/<int:rid>/',views.Reply,name='Reply'),

    path('Viewfeedback/',views.Viewfeedback,name='Viewfeedback'),

    path('Propertytype',views.Propertytype,name='Propertytype'),
    path('delpropertytype/<int:did>',views.delpropertytype,name='delpropertytype'),
    path('editpropertytype/<int:eid>/',views.editpropertytype,name='editpropertytype'),




]
