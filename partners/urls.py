from django.urls import path

from partners.views.customer import CustomerListView
from partners.views.partner import PartnerListView

app_name = 'partners'
urlpatterns = [
    path('partners', PartnerListView.as_view(), name='partner-list'),
    path('customers', CustomerListView.as_view(), name='customer-list'),
]
