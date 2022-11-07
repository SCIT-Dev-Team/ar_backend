from rest_framework import serializers

from main.models import Artifact, Category


class CategorySearializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ArtifactSearializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = "__all__"