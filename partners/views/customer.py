from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from partners.filters import CustomerFilter
from partners.models import Customer
from partners.serializers.customer import CustomerSerializer


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerFilter
