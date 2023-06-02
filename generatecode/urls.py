from django.urls import path
from generatecode.views import QRcodeApiView

urlpatterns = [
    path('api/qrcode/', QRcodeApiView.as_view(), name='qrcode'),
]