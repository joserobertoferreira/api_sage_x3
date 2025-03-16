from django_filters import rest_framework as filters

from partners.models import Partner


class PartnerFilter(filters.FilterSet):
    company_name_0 = filters.CharFilter(lookup_expr='icontains')
    company_name_1 = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Partner
        fields = (
            'company_name_0',
            'company_name_1',
        )
