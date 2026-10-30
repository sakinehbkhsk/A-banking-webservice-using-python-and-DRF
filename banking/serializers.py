

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
       


class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    def validate_amount(self,value):
        if value <= 0:
            raise serializers.ValidationError (" Amount must be positive and greater than zero.")
        return value