from rest_framework import serializers

from partners.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    addresses = serializers.CharField(source='get_addresses', read_only=True)

    class Meta:
        model = Customer
        fields = (
            'customer',
            'company_name',
            'currency',
            'create_user',
            'create_date',
            'update_user',
            'update_date',
            'addresses',
        )
