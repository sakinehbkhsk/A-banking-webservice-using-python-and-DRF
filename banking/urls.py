

from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerDetailView, AccountListView, AccountCreateView, AccountDetailView, CustomerAccountsView, CreditAccountView, DebitAccountView
urlpatterns = [

    #customer urls
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:customer_no>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:customer_no>/accounts/', CustomerAccountsView.as_view(), name='customer-accounts'),

    #account urls
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path ('accounts/create/', AccountCreateView.as_view(), name='account-create'),
    path('accounts/<str:account_no>/', AccountDetailView.as_view(), name='account_detail'),

    #Transaction urls
    path ('accounts/<str:account_no>/credit/', CreditAccountView.as_view(), name='credit_account'),
    path('accounts/<str:account_no>/debit/', DebitAccountView.as_view(), name='debit_account'),
    ]
