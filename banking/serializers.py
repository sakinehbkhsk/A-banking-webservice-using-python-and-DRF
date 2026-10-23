

from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def validate_national_code(self,value):
        if len(value) != 10:
            raise serializers.ValidationError(
                "National code must be exactly 10 digits."
            )

        if not value.isdigit():
            raise serializers.ValidationError(
                "National code must contain only digits."
            )


        return value
