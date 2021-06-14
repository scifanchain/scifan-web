from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SigninView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', SigninView.as_view(), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stage/<int:id>/', views.stage, name='stage'),
]
