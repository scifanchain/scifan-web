from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def index(request):
    return HttpResponse('This ia accounts index')


def register(request):
    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('successfully')
                else:
                    return HttpResponse('不合法的用户')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    return HttpResponse('您已注销。')


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})