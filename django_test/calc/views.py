from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def home (request ):
    return render(request,'home.html',{'name':'ahmed'});


def add (request):
    val1=int(request.GET['val1']);
    val2=int(request.GET['val2']);
    res=val1+val2
    return render(request,'result.html',{'result':res})


def index(request):
    return render(request,'index.html')

def account_login(request):
    return render(request,'auth/signup.html')

def new_user(request):
   
    
    username=request.GET['name'];
    email=request.GET['email'];
    password=request.GET['password'];
    mobile=request.GET['mobile'];
    
     new_user=User();
    new_user.name=username;
    new_user.email=email;
    new-user.password=password;
    new-user.mobile=mobile;
    
    return render(request,'auth/signup.html');