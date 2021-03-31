from rest_framework import serializers

class UploadImageSerializer(serializers.Serializer):
    option = serializers.CharField(max_length=2)
    original_image = serializers.CharField()
