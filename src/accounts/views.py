import django
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse('This ia accounts index')


def signup(request):
    return render(request, 'accounts/signup.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})