from django.urls import path
from .views import CNABView

urlpatterns = [
    path('cnab/upload/', CNABView.as_view(), name='cnab_upload'),
]