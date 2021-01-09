from django.contrib import admin
from django.urls import path,include
from .views import signup, userName
from . import views
urlpatterns = [
    
    path('register',views.signup,name='register'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name='logut'),
    path('user',views.userName,name='user')
]
