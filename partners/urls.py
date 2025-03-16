from django.urls import path

from partners.views import PartnerListView

app_name = 'partners'
urlpatterns = [
    path('partners', PartnerListView.as_view(), name='partner-list'),
]
