

from django.urls import path
from .views import create_customer, all_customers, customer

urlpatterns = [

    path('customers/', create_customer, name='create_customer'),
    path('customers/all', all_customers, name='all_customers'),
    path('customers/{id}', customer, name='customer'),
]
