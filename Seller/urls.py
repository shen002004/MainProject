
from django.urls import path
from Seller import views

app_name='Seller'

urlpatterns = [
        path('Myprofile/',views.Myprofile,name='Myprofile'),
        path('Editprofile/',views.Editprofile,name='Editprofile'),         
        path('Changepas/',views.Changepas,name='Changepas'),               
        
        path('Home/',views.Home,name='Home'),
        
        path('Addproperty/',views.Addproperty,name='Addproperty'),
        path('delpro/<int:did>',views.delpro,name='delpro'),

        
        path('Gallery/<int:pid>',views.Gallery,name='Gallery'),
        path('delgal/<int:did>/<int:id>',views.delgal,name='delgal'),   


        path('Complaint/',views.Complaint,name='Complaint'),
        path('delcom/<int:did>',views.delcom,name='delcom'),

        path('Feedback/',views.Feedback,name='Feedback'),

        path('Viewbooking/',views.Viewbooking,name='Viewbooking'),
        path('acceptbuying/<int:act>',views.acceptbuying,name='acceptbuying'),
        path('rejectbuying/<int:rej>',views.rejectbuying,name='rejectbuying'),


]
