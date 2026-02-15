from django.urls import path
from User  import views

app_name='User'
urlpatterns = [
    path('Home/',views.Home,name='Home'),
    
    path('Myprofile/',views.Myprofile,name='Myprofile'),

    path('Editprofile/',views.Editprofile,name='Editprofile'),   
     
    path('Changepas/',views.Changepas,name='Changepas'),
    
    path('Viewpro/',views.Viewpro,name='Viewpro'),
    
    path('Buy/<int:pid>/', views.Buy, name='Buy'),
    
    path('Myprobooking/',views.Myprobooking,name='Myprobooking'),
    path('delbuy/<int:did>',views.delbuy,name='delbuy'),

    path('ViewGallery/<int:pid>/',views.ViewGallery,name='ViewGallery'),

    path('PropertyRent/<int:pid>',views.PropertyRent,name='PropertyRent'),

    path('MyproRent/',views.MyproRent,name='MyproRent'),
    path('delrent/<int:did>',views.delrent,name='delrent'),

    path('AddPayment/<int:bid>',views.AddPayment,name='AddPayment'),

    path('Paymenthistory/<int:bid>',views.Paymenthistory,name='Paymenthistory'),

    path('Complaint/',views.Complaint,name='Complaint'),
    path('delcom/<int:did>',views.delcom,name='delcom'),

    path('Feedback/',views.Feedback,name='Feedback'),
    path('Ajaxpro/',views.Ajaxpro,name='Ajaxpro'),

    path('Proviewmore/<int:id>',views.Proviewmore,name='Proviewmore'),

    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),


]