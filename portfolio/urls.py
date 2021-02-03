from .views import CustomerList
from django.urls import path

urlpatterns = [
    path('customer_list/', CustomerList.as_view(), name='customer_list'),
]