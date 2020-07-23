from django.shortcuts import render,redirect
from django.http import HttpResponse
import pyrebase

config={
    "apiKey": "AIzaSyD9IgyOi1idiVXUq5a3SIQdM_RF6P9arr4",
    "authDomain": "glean-998ba.firebaseapp.com",
    "databaseURL": "https://glean-998ba.firebaseio.com",
    "projectId": "glean-998ba",
    "storageBucket": "glean-998ba.appspot.com",
    "messagingSenderId": "946690750269",
    "appId": "1:946690750269:web:2b114562cb8d7241d2b754",
    "measurementId": "G-L3QDY8PYDL"
}

firebase=pyrebase.initialize_app(config)
database=firebase.database()
auth=firebase.auth()

def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def aftersignin(request):
    email = request.POST.get("email")
    password = request.POST.get("password") 
    try:
        user = auth.sign_in_with_email_and_password(email,password)
    except:
        message="Invalid Credentials"
        return render(request, 'signin.html',{'message':message})
    return render(request, 'index.html')

def aftersignup(request):
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    password = request.POST.get('Password')
    cpassword = request.POST.get('CPassword')
    try:
        user=auth.create_user_with_email_and_password(email,password)
    except:
        message="unable to create account...Try Again !!"
        return render(request, 'signup.html', {'message':message})
        uid=user['localId']
    
    data={'name':name, 'status':'1'}

    database.child('users').child('uid').child('details').set(data)

    return render(request,'signin.html')

