from django.contrib import admin

from main import models

admin.site.register(models.Category)
admin.site.register(models.Artifact)

