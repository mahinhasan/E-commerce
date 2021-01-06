from django.urls import path,include
from . import views
urlpatterns = [
    
    path('store/',views.index,name='home')

    
]