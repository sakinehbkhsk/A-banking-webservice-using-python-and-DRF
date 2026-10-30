

from django.urls import path
from .views import create_customer, all_customers

urlpatterns = [

    path('customers/', create_customer, name='create_customer'),
    path('customers/', all_customers, name='all_customers'),
]
