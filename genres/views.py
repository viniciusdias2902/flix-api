from django.http import JsonResponse
from genres.models import Genre
from django.views import View

class GenreView(View):
    def get(self, request, *args, **kwarg):
        genres = Genre.objects.all()
        data = [{'id' : genre.id, 'name' : genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    def post(self, request, *args, **kwargs):
        pass
