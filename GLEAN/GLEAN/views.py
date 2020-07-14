from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')