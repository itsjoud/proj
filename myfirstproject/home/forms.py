from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__'


# class CreateUserForm(UserCreationForm):
#     class Meta:
#          model = Order
#          fields=['username','email','password1', 'password2']
# 
# 
# 
# # from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User