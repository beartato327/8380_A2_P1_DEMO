from django.urls import path
from .views import (
    CustomerList,
    CustomerDelete,
    CustomerUpdate,
    CustomerCreate,
    HomeView,
    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('customer_list', CustomerList.as_view(), name='customer_list'),
    path('customer_add', CustomerCreate.as_view(), name='customer_add'),
    path('customer/<int:pk>/edit', CustomerUpdate.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer_delete'),
]