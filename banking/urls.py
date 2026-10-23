

from django.urls import path
from .views import create_customer

urlpatterns = [

    path('customers/', create_customer, name='create_customer'),
]
