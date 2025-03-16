from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls', namespace='accounts')),
    path('api/v1/partners/', include('partners.urls', namespace='partners')),
]
