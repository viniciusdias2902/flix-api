from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreView.as_view(), name='genre-list'),
]
