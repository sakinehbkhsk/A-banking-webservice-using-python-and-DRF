from django.shortcuts import render, get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Customer,Account

from .serializers import CustomerSerializer, AccountSerializer, TransactionSerializer


class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get (self, request, customer_no):
        customer = get_object_or_404(Customer, pk=customer_no   )
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountListView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountCreateView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    def get(self, request, account_no):
        account = get_object_or_404(Account,account_no=account_no)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerAccountsView(APIView):
    def get(self, request, customer_no):
        accounts = Account.objects.filter(customer_id=customer_no)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CreditAccountView(APIView):
    def post(self, request, account_no):
        account = get_object_or_404(Account, account_no=account_no)
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
    
        if account.account_status == Account.AccountStatus.CLOSED:
            return Response({"error":"Account is closed."}, status=status.HTTP_403_FORBIDDEN)
    
        account.account_balance += amount
        account.save(update_fields=['account_balance'])
        return Response({"message": "Credit successful.", "account_no": account.account_no,
                            "account_balance": account.account_balance}, status=status.HTTP_200_OK)


class DebitAccountView(APIView):
    def post(self, request, account_no):
        account = get_object_or_404(Account, account_no=account_no)
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
    
        if account.account_status != Account.AccountStatus.OPEN:
            return Response({"error":"Account is not OPEN."}, status=status.HTTP_403_FORBIDDEN)
    
        if amount > account.account_balance:
            return Response({"error":"Insufficient funds"},status=status.HTTP_400_BAD_REQUEST)
        
        account.account_balance -= amount
        account.save(update_fields=['account_balance'])
        return Response({"message":"Debit successful.", "account_no": account.account_no,
                            "account_balance": account.account_balance}, status=status.HTTP_200_OK)

        






            
    

    
    