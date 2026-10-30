

from rest_framework import serializers
from .models import Customer, Account

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name']
        read_only_fields = ['id']



class AccountSerializer(serializers.ModelSerializer):
    customer_no = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all(), source = 'customer')
    class Meta:
        model = Account
        fields = ['id', 'account_no', 'customer_no', 'account_status', 'account_balance']
        read_only_fields = ['id', 'account_status', 'account_balance']
