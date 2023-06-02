from rest_framework import serializers


class QRCodeSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=255)


