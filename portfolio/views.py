from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Customer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = "portfolio/home.html"

class CustomerList(LoginRequiredMixin,ListView):
    model = Customer

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone']

class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')

class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['cust_number','name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone']
    success_url = reverse_lazy('customer_list')