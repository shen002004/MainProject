from django.urls import path
from Guest  import views
app_name='Guest'
urlpatterns = [   
        path('UserReg/',views.UserReg,name='UserReg'),

        path('Home/',views.Home,name='Home'),

        path('Login/',views.Login,name='Login'),
                        
        path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
        
        path('Seller/',views.Seller,name='Seller'),
        
        path('Renterreg/',views.Renterreg,name='Renterreg'),
]