
from django.contrib.auth import views as auth_views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('login/', views.LoginPage, name="login" ), 
]

