from Store.models import Category, Product
from django.shortcuts import render

# Create your views here.

def index(request):

    product = Product.get_all_products()
    categories = Category.get_all_category()

    data  = {}
    data['product'] = product
    data['categories']=categories

    return render(request,'index.html',data)