from django.urls import path

from main import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailApiView.as_view()),
    path('artifacts/', views.ArtifactListApiView.as_view()),
    path('artifacts/<int:pk>/', views.ArtifactDetailApiView.as_view()),
]