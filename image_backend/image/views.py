from django.shortcuts import render
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from image.models import Images
from image.serializers import UploadImageSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile


from PIL import Image
from io import BytesIO
import base64
import uuid
import sys

class UploadView(views.APIView):
    def post(self, request):
        try:
            serializer = UploadImageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            option = data.get('option')
            origin_image = data.get('original_image').split(",")[-1]
            original_file = None
            square_file = None
            small_file = None

            # Image Validation
            try:
                img = Image.open(BytesIO(base64.b64decode(origin_image)))
            except Exception as e:
                return Response(data={
                    "message": "Please select image file",
                    "code": status.HTTP_400_BAD_REQUEST
                })
            file_format = img.format
            if option == 'SQ' or option == 'AL':
                img = img.resize(
                    (img.width, img.width), Image.ANTIALIAS)
                square_file = BytesIO()
                img.save(square_file, format=f"{file_format}")
                square_file=InMemoryUploadedFile(square_file, None, 'foo.jpg', 'image/jpeg', len(square_file.getvalue()), None)
            if option == 'SM' or option == 'AL':
                img = img.resize((256, 256), Image.ANTIALIAS)
                small_file = BytesIO()
                img.save(small_file, format=f"{file_format}")
                small_file=InMemoryUploadedFile(small_file, None, 'foo.jpg', 'image/jpeg', len(small_file.getvalue()), None)
            if option == 'OG' or option == 'AL':
                original_file = BytesIO()
                img.save(original_file, format=f"{file_format}")
                original_file=InMemoryUploadedFile(original_file, None, 'foo.jpg', 'image/jpeg', len(original_file.getvalue()), None)
            try:
                Images.objects.create(
                    uuid = uuid.uuid4(),
                    option=option,
                    original_file=original_file,
                    small_file=small_file,
                    square_file=square_file,
                )
            except Exception as e:
                return Response(data={
                    "message": f"Can not save image: {e}",
                    "code": status.HTTP_400_BAD_REQUEST
                })

            return Response(data={
                "message": "Save image successfully",
                "code": status.HTTP_200_OK
            })
        except Exception as e:
            print(e)
            return Response(data={
                "message": "Failed saving image",
                "code": status.HTTP_400_BAD_REQUEST
            })
