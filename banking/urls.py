

from django.urls import path
from .views import create_customer, all_customers, customer, list_customers, create_account, all_accounts, account_detail, customer_accounts

urlpatterns = [

  
    path('customers/', create_customer, name='create_customer'),
    path('customers/all', all_customers, name='all_customers'),
    path('customer/<int:id>/', customer, name='customer'),
    path('customers/<int:customer_no>/accounts/', customer_accounts, name='cusotmer_accounts'),
    
    path('customers/', list_customers, name='list_customers'),
    path('customers/<int:id>', list_customers, name='customer'),

    path('accounts/', create_account, name='create_account'),
    path ('accounts/all', all_accounts, name='all_accounts'),
    path('accounts/<int:id>/', account_detail, name='account_detail'),
    ]
