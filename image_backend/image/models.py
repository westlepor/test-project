from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings
from image.utils import PathAndRename
import uuid

OUTPUT_OPTIONS = (
    ('OG', 'ORIGINAL'),
    ('SQ', 'SQUARE SIZE'),
    ('SM', 'SMALL'),
    ('AL', 'ALL')
)

original_path = PathAndRename('output_images/original')
square_path = PathAndRename('output_images/square')
small_path = PathAndRename('output_images/small')

# Test with local storage and S3 storage
fs = S3Boto3Storage() if settings.USE_S3 else FileSystemStorage()

class Images(models.Model):

    uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    option = models.CharField(max_length=2, choices=OUTPUT_OPTIONS, default='OG')
    original_file = models.ImageField(upload_to=original_path,
                                    storage=fs,
                                    null=True,
                                    blank=True)
    square_file = models.ImageField(upload_to=square_path,
                                    storage=fs,
                                    null=True,
                                    blank=True)
    small_file = models.ImageField(upload_to=small_path,
                                    storage=fs,
                                    null=True,
                                    blank=True)

    class Meta:
        db_table='image'
        verbose_name = 'image'
        verbose_name_plural = 'images'
