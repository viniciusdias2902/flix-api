from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreListView, GenreDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail-update'),
]
