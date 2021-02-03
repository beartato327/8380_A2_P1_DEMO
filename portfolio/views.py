from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer

# Create your views here.
class CustomerList(ListView):
    model = Customer