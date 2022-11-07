from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)


def _get_file_extension(filename):
    return filename.split('.')[-1]

def upload_artifact_image(artifact, filename):
    return f'media/artifacts/images/{artifact.id}.{_get_file_extension(filename)}'


def upload_artifact_model(artifact, filename):
    return f'media/artifacts/models/{artifact.id}.{_get_file_extension(filename)}'

class Artifact(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.FileField(upload_to=upload_artifact_image, max_length=255)
    model = models.FileField(upload_to=upload_artifact_model, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)