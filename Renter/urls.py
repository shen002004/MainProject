from django.urls import path
from Renter import views

app_name='Renter'
urlpatterns = [
    path('Home/',views.Home,name='Home'),
    
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepas/',views.Changepas,name='Changepas'),
    
    
    path('Addproperty/',views.Addproperty,name='Addproperty'),
    path('delpro/<int:did>',views.delpro,name='delpro'),
    path('acceptpro/<int:act>',views.acceptpro,name='acceptpro'),
    path('rejectpro/<int:rej>',views.rejectpro,name='rejectpro'),

    path('Viewbookings/',views.Viewbookings,name='Viewbookings'),

    
    path('Gallery/<int:pid>',views.Gallery,name='Gallery'),
    path('delgal/<int:did>/<int:id>',views.delgal,name='delgal'),        

    path('Complaint/',views.Complaint,name='Complaint'),
    path('delcom/<int:did>',views.delcom,name='delcom'),

    path('Feedback/',views.Feedback,name='Feedback'),



]