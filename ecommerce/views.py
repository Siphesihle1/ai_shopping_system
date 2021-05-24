# Django HTTP
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime        

# Django Login
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Django Registration
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from .forms import UserForm, CustomerForm, OrderForm, LoginForm

# Django geolocation
from django_ip_geolocation.decorators import with_ip_geolocation

# Misc
from .models import *
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic import TemplateView


# Create your views here.

@with_ip_geolocation
def store(request):
    if request.user.is_authenticated:
        u = request.user
        customer = Customer.objects.get(user_id=u.id)
        
        # Get the user's location
        location = request.geolocation
        if (location["geo"]):
            customer.latitude = location["geo"]["latitude"]
            customer.longitude = location["geo"]["longitude"]
            u.save()

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = 0

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}

    return render(request, 'ecommerce/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        u = request.user
        customer = Customer.objects.get(user_id=u.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
        context = {'items':items, 'order':order, 'cartItems':cartItems}
        return render(request, 'ecommerce/cart.html', context)
    else:
        return redirect('login')


@csrf_exempt
def checkout(request):
    
    if request.user.is_authenticated:
        u = request.user
        customer = Customer.objects.get(user_id=u.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        total = order.get_cart_total

        context = {'items':items, 'order':order, 'cartItems':cartItems, 'total':total}
        return render(request, 'ecommerce/checkout.html', context)
    else:
        return redirect('login')

def updateItem(request):
    
    if request.user.is_authenticated:
        data=json.loads(request.body)
        productId = data['productId']
        action = data['action']
        #print('Action:', action)
        #print('Product:', productId)

        u = request.user
        customer = Customer.objects.get(user_id=u.id)

        product = Product.objects.get(id=productId)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
          
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        if orderItem.quantity <= 0:
            orderItem.delete()
        else:
            orderItem.save()

        return JsonResponse({'message': 'Item updated'}, safe=False)
    else:
        return redirect('login')

    
@csrf_exempt
def processOrder(request):
    
    if request.user.is_authenticated:
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        u = request.user
        customer = Customer.objects.get(user_id=u.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = data['form']['total']
        order.transaction_id = transaction_id
        print(total, transaction_id)

        if total == order.get_cart_total:
            order.complete = True
            order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )


        return JsonResponse('Payment Complete', safe=False)
    else:
        return redirect('login')


@login_required
def deletefromcart(request, id):
    
    # Get customer info
    u = request.user
    customer = Customer.objects.get(user_id=u.id)
    product = Product.objects.get(id=id)

    # Get the order item
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # Delete the order item
    if (orderItem):
        orderItem.delete()
    
    # Get the new order items
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()   
    cartItems = order.get_cart_items
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'ecommerce/cart.html', context)

@login_required
def emptyCart(request):

    # Get customer information
    u = request.user
    customer = Customer.objects.get(user_id=u.id)

    # Get order information
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    # Delete order
    order.delete()

    # Get the new order items
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()   
    cartItems = order.get_cart_items
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'ecommerce/cart.html', context)

@login_required
def storeCustomerActivity(request):

    # Get customer information
    u = request.user
    customer = Customer.objects.get(user_id=u.id)
    
    # Get activity data
    data = json.loads(request.body)
    
    product_id = data["product_id"]
    action = data["action"]

    product = Product.objects.get(id=product_id)
    
    # Store the information
    if (action == 'add'):
        customerActivity = CustomerActivity.objects.create(
            customer=customer, 
            product=product, 
            action=CustomerActivity.ADD
        )
    else:
        customerActivity = CustomerActivity.objects.create(
            customer=customer, 
            product=product, 
            action=CustomerActivity.VIEW
        )

    customerActivity.save()
    
    return JsonResponse({"message": "{} {}ed the {}".format(customer, action, product)}, safe=False)

@login_required
def customer_activity(request):

    # Get customer info
    u = request.user
    customer = Customer.objects.get(user_id=u.id)

    # Get activity logs for customer
    logs = CustomerActivity.objects.filter(customer=customer, action = CustomerActivity.VIEW).order_by('-event_date')[:20] 

    # Get the order items
    order, created = Order.objects.get_or_create(customer=customer, complete=False) 
    cartItems = order.get_cart_items

    context = {"activity_logs": logs, "cartItems": cartItems}

    return render(request, 'ecommerce/useractivity.html', context)

def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            
            user = user_form.save()
            user.refresh_from_db() # reloading the database
            user.customer.cellphone_no = customer_form.cleaned_data['cellphone_no']
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
        else:
            context = {'user_form' : user_form, 'customer_form': customer_form}
            return render(request, 'ecommerce/signup.html', context)
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

        context = {'user_form' : user_form, 'customer_form': customer_form}
        return render(request, 'ecommerce/signup.html', context)

def Login(request):

    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == 'POST':

            login_form = LoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('store')
            else:
                messages.error(request, 'Username OR password is incorrect')
                return render(request, 'ecommerce/login.html', {'form' : login_form})

        else:
            login_form = LoginForm()
            context = {'form' : login_form}
            return render(request, 'ecommerce/login.html', context)

@login_required
def Logout(request):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect('store')

@login_required
def order_history(request):

    # Get customer info
    u = request.user
    customer = Customer.objects.get(user_id=u.id)

    # Get activity logs for customer
    logs = CustomerActivity.objects.filter(customer=customer).all()

    # Get the previous orders
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    orders = Order.objects.filter(customer=customer).all()

    context = {"orders": orders, "cartItems": cartItems}

    return render(request, 'ecommerce/orderhistory.html', context)   

@csrf_exempt
def PurchaseHistory(request):
    
    if request.user.is_authenticated:

        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        u = request.user
        customer = Customer.objects.get(user_id=u.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = order.get_cart_total

        if order.complete == True:
            p = PurchaseHistory(username = customer, order = customer, date_added = order.transaction_id, state = 'Delivered')
            p.save()

        return JsonResponse('Stored', safe=False)
    else:
        return redirect('store')


