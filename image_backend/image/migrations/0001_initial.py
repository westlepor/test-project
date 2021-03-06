# Generated by Django 3.1.7 on 2021-03-31 14:31

from django.db import migrations, models
import image.utils
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('option', models.CharField(choices=[('OG', 'ORIGINAL'), ('SQ', 'SQUARE SIZE'), ('SM', 'SMALL'), ('AL', 'ALL')], default='OG', max_length=2)),
                ('original_file', models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=image.utils.PathAndRename('output_images/original'))),
                ('square_file', models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=image.utils.PathAndRename('output_images/square'))),
                ('small_file', models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=image.utils.PathAndRename('output_images/small'))),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'image',
            },
        ),
    ]
