from django.shortcuts import render, get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,Account

from .serializers import CustomerSerializer, AccountSerializer, TransactionSerializer

"""
customer part with different views ... create customer, all customers , customer
"""

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
           serializer.data,
           status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
def all_customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def customer(request,id):
    data = get_object_or_404(Customer, pk=id)
    serializer = CustomerSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""
 customer part with just one view ...

"""

@api_view(['GET', 'POST'])
def list_customers(request, id=None):
    if request.method == 'GET':
        if id is None:
            data = Customer.objects.all()
            serializer = CustomerSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = get_object_or_404(Customer, pk=id)
            serializer = CustomerSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_accounts(request):
    data= Account.objects.all()
    serializer = AccountSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def account_detail(request,account_no):
    data = get_object_or_404(Account,account_no=account_no)
    serializer = AccountSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def customer_accounts(request,customer_no):
    data = Account.objects.filter(customer_id=customer_no)
    serializer = AccountSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def credit_account(request,account_no):
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


@api_view(['POST'])
def debit_account(request,account_no):
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