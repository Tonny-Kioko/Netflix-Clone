import email
from django import views
from django.shortcuts import render, redirect
from django.views import View 
from .models import CustomUser, Movie, Video, Profile
from django.db.models import Q
from django.contrib import messages
from . forms import MyUserCreationForm, ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect ('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower() 
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(email=email)
        except:
            messages.error(request, "This profile is unavailable")
        
        customuser = authenticate(request, email=email, password=password)

        if customuser is not None:
            login(request, customuser)
            return redirect ('home')
        else:
            messages.error(request, "Username does not Exist")
        
        context = {'page': 'page'}
        return render(request, 'profileCreate.html', context)


def logoutProfile(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            customuser = form.save(commit=False)
            customuser.username = customuser.username.lower()
            customuser.save()
            login(request, customuser)
            return redirect ('home')
        else:
            messages.error(request, "An error occurred in Registration")
    
    context = {'form': 'form'}
    return render (request, 'profileCreate.html', context) 





def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    movies = Movie.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(cast__icontains=q) |
        Q(genre__icontains=q) 
    )

    movies = Movie.objects.all()

    context = {'movies': 'movies'}
    return render(request, 'home.html', context)