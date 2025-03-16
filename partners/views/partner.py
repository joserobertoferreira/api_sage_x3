from rest_framework.response import Response
from rest_framework.views import APIView

from partners.filters import PartnerFilter
from partners.models import Address, Partner
from partners.serializers.partner import PartnerSerializer


class PartnerListView(APIView):
    @staticmethod
    def get(request):
        queryset = Partner.objects.filter()
        filter = PartnerFilter(request.GET, queryset=queryset)
        partners = PartnerSerializer(filter.qs, many=True)

        for partner in partners.data:
            partner['addresses'] = Address.objects.filter(
                entity_number=partner['bp']
            ).values(
                'address_line_0',
                'address_line_1',
                'address_line_2',
                'country',
                'country_name',
            )

        return Response(partners.data)
