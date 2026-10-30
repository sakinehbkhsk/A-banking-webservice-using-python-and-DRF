from django.shortcuts import render, get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,Account

from .serializers import CustomerSerializer, AccountSerializer

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
def account_detail(request,id):
    data = get_object_or_404(Account,pk=id)
    serializer = AccountSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def customer_accounts(request,customer_no):
    data = Account.objects.filter(customer_id=customer_no)
    serializer = AccountSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def credit_account(request,account_no):
    ...