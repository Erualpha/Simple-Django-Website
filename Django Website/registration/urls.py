
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),    
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'), 
    
]
