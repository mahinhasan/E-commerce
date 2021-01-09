from typing import Tuple
from django import template

register = template.Library()
#check product is in cart
@register.filter(name='is_In_cart')
def is_In_cart(p,cart):
    keys = cart.keys()
    for k in keys:
        if int(k) == (p.id):
            return True
    return False
#how many iteam added to cart
@register.filter(name='cart_quantity')
def cart_quantity(p,cart):
    #access keys
    keys = cart.keys()      
    for k in keys:
        #check product is in cart
        if int(k) == (p.id):
            #pass keys means quantatiy of product to the server one by one 
            return cart.get(k)         
    return 0
    

@register.filter(name='total_price')
def total_price(p,cart):
    return  p.price * int(cart_quantity(p,cart))  


@register.filter(name='grand_total')
def grand_total(product,cart):
    sum = 0
    for x in product:
        sum += total_price(x,cart)
    return sum


@register.filter(name='currency')
def currency(number):
    return "৳"+str(number)


@register.filter(name='multipy')
def multipy(num,n):
    return num*n
