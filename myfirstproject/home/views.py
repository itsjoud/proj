from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from .forms import OrderForm, CreateUserForm
from .forms import OrderForm
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'signin.html')


def signup(request):
    # form=CreateUserForm()

    # if request.method == 'POST':
    #     form=CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    # context={'form':form}
    return render(request, 'signup.html')
# , context

def items(request):
    items= Product.objects.all()
    return render(request, 'home/items.html',{'items':items})

def customer(request,pk):

    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()

    context={"customer": customer, "orders":orders, "order_count":order_count}

    return render(request, 'home/customer.html',context)

def Admin(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()

    total_orders=orders.count()
    paid=orders.filter(status="Paid").count()
    pending=orders.filter(status="Pending").count()


    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'paid':paid, 'pending':pending}
# 'total_customers':total_customers,
    return render(request, 'home/admin.html', context)

def product(request):
    product= Product.objects.all()
    return render(request, 'home/adminitems.html',{'product':product})


def AdmincreateOrder(request,pk):
     OrderFormSet= inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10)
     customer= Customer.objects.get(id=pk)
     formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
     if request.method=="POST":
            formset=OrderFormSet(request.POST, instance=customer)
            if formset.isvalid():
                formset.save()
                return redirect('Admin')
     context={'formset':formset}
     return render(request,'home/admin_order_form.html', context)

def createOrder(request,pk):
     OrderFormSet= inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10)
     customer= Customer.objects.get(id=pk)
     formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
     if request.method=="POST":
            formset=OrderFormSet(request.POST, instance=customer)
            if formset.isvalid():
                formset.save()
                return redirect('home')
            
     context={'formset':formset}
     return render(request,'home/order_form.html', context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method =='POST':
            form= OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect ('Admin')
    
    context={'form': form}
    return render(request, 'home/admin_order_form.html', context)
    

def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('Admin')
    
    context={"item":order}
    return render(request,'home/delete.html', context)
   