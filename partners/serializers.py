from rest_framework import serializers

from partners.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    addresses = serializers.CharField(source='get_addresses', read_only=True)

    class Meta:
        model = Partner
        fields = (
            'bp',
            'company_name_0',
            'company_name_1',
            'european_vat_number',
            'country',
            'currency',
            'language',
            'is_customer',
            'is_supplier',
            'create_user',
            'create_date',
            'update_user',
            'update_date',
            'addresses',
        )
