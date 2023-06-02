from io import BytesIO

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
import qrcode
from rest_framework.views import APIView

from generatecode.serizlizers import QRCodeSerializer


class QRcodeApiView(APIView):
    def post(self, request):
        serializer = QRCodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data['data']

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,

            )
            qr.add_data(data)
            qr.make(fit=True)
            image = qr.make_image(fill_color="black", back_color="white")

            # Save the image to a BytesIO object
            image_io = BytesIO()
            image.save(image_io, format='PNG')
            image_io.seek(0)

            # Return the image as a response
            return HttpResponse(image_io, content_type='image/png')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
