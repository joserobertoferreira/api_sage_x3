from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings


class APIPagination(PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    page_size_query_param = settings.PAGE_SIZE_QUERY_PARAM
    max_page_size = settings.MAX_PAGE_SIZE
