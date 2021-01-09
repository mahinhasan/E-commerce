from account.models import Customer
from Store.models import Category, Order, Product
from django.shortcuts import redirect, render
from django.views import View
from account.models import Customer
# Create your views here.

class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        
        # print(remove)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:    
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('/')
            
        
        
    def get(self,request):
        #clear the cokkies
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        customer = Customer.objects.all()
        categories = Category.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:
            product=Product.get_all_products_by_id(categoryID)
        else:
            product=Product.get_all_products()
        data  = {}
        data['product'] = product
        data['categories']=categories
        data['customer'] = customer
        # print(request.session.get('email'))
        # print(request.session.get('customer_id'))
        return render(request,'index.html',data)




class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        product = []
       
        product = Product.objects.filter(id__in=ids)
           
        return render(request,'cart.html',{'product':product})
        


class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list( cart.keys()))

        for p in product:
            order = Order(
                customer=Customer(id=customer),
                product = p,
                price = p.price,
                address =address,
                phone = phone,
                quantity = cart.get(str(p.id))

            )
            order.save()
        request.session['cart'] = {}

        #print(address,phone,customer,cart,product)
        return redirect('cart')





class OrderList(View):
    def get(self,request):
        customer = request.session.get('customer')
        print(customer)
        orders = Order.get_order_by_customer_id(customer)
        
        return render(request,'order.html',{'orders':orders})


