from django.http import JsonResponse
from genres.models import Genre
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class GenreView(View):
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all()
        data = [{'id' : genre.id, 'name' : genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        if data['name']:
            new_genre = Genre(name=data['name'])
            new_genre.save()
            return JsonResponse({'id' : new_genre.id, 'name': new_genre.name}, status=201)
        else:
            return JsonResponse({'error' : 'bad request'}, status=400)
