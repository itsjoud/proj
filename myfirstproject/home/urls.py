from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
     path('home', views.home, name='home'),
     path('signin', views.signin, name='signin'),
     path('signup', views.signup, name='signup'),
     path('items', views.items, name='items'),
     path('customer/<str:pk>', views.customer, name='customer'),
     path('Admin', views.Admin, name='Admin'),
     path('product', views.product, name='product'),
     path('admin_create_order/<str:pk>', views.AdmincreateOrder, name='admin_create_order'),
     path('create_order', views.createOrder, name='create_order'),
     path('update_order/<str:pk>', views.updateOrder,name= "update_order"),
     path('delete_order/<str:pk>', views.delete, name='delete_order'),
]
