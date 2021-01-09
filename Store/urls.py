from django.urls import path,include
from . import views
from .views import Cart, Index,Checkout,OrderList
urlpatterns = [
    
    #path('',views.index,name='store')
    path('',Index.as_view(),name='home'),
    path('cart',Cart.as_view(),name='cart'),
    path('checkout',Checkout.as_view(),name='checkout'),
    path('order',OrderList.as_view(),name='order')
    
]