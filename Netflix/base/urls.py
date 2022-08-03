
from django.contrib.auth import views as auth_views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('login/', views.loginPage, name="login" ), 
    path('logout/', views.logoutProfile, name="logout" ),

    path('register/', views.registerUser, name="register" ),
    
]

