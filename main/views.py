from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from main.models import Artifact, Category
from main.serializers import ArtifactSearializer, CategorySearializer


class CategoryListApiView(generics.ListCreateAPIView):
    serializer_class = CategorySearializer
    queryset = Category.objects.all()


# TODO - disable delete api view in production
class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySearializer
    queryset = Category.objects.all()


class ArtifactListApiView(generics.ListCreateAPIView):
    serializer_class = ArtifactSearializer
    queryset = Artifact.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    

# TODO - disable delete api view in production
class ArtifactDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtifactSearializer
    queryset = Artifact.objects.all()
