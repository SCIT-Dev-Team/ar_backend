import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)


def _get_file_extension(filename):
    return filename.split('.')[-1]

def upload_artifact_image(artifact, filename):
    return f'artifacts/images/{datetime.datetime.now().timestamp()}.{_get_file_extension(filename)}'


def upload_artifact_model(artifact, filename):
    return f'artifacts/models/{datetime.datetime.now().timestamp()}.{_get_file_extension(filename)}'

class Artifact(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.FileField(upload_to=upload_artifact_image, max_length=255)
    model = models.FileField(upload_to=upload_artifact_model, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['category', 'name']