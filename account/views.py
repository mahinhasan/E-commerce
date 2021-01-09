from account.models import Customer
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import make_password, check_password
from .models import Customer

# Create your views here.


def signup(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        postData = request.POST

        first_name = postData.get('fname')
        last_name = postData.get('lname')
        email = postData.get('email')
        phone = postData.get('phone')
        address = postData.get('address')
        password = postData.get('password')

        customer = Customer(first_name=first_name, last_name=last_name,
                            email=email, phone=phone, address=address, password=password)

        # validition
        error = None
        if not first_name:
            error = "First Name Required!"

        elif customer.isExist():
            error = "Email already exists"

        # value

        # Saving

        if not error:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('')
        else:
            return render(request, 'register.html', {'error': error})
    return render(request, 'register.html')


def login(request):

    
    users = Customer.objects.all()
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        postData = request.POST

        login_erro = None
        username = postData.get('fname')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer.get_customer_by_email(email)

        for c in customer:
            p = c.password
            u = c.first_name
            i = c.id
        
            e = c.email
        if customer:

            if username == u:

                f = check_password(password, p)
                if f:
                    #save customer as id and email to session
                    request.session['customer'] = i
                    request.session['customer'] = u
                    request.session['email'] = e

                    return redirect('/')
                else:
                    login_erro = "wrong password!!"
            else:
                login_erro = "wrong username"
        else:
            login_erro = "Email or password Invalid!"

        return render(request, 'login.html', {'error': login_erro,'user':u,'users':users})
       

def logout(request):
    request.session.clear()
    return redirect('/')


# def userName(request):
#     customer = request.session.get('customer')

#     customer_name = Customer.get_customer_by_id(customer)
#     for c in customer_name:
#         u = c.first_name
#         print(u)
#     return render(request,'base.html',{'name':u})

def userName(request):
    cus = request.session.get('customer')
    customer = Customer.objects.get(id=cus)

    return render(request,'base.html',{'customer':customer})
