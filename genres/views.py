from django.http import JsonResponse
from genres.models import Genre
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework import generics
import json
from genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# @method_decorator(csrf_exempt, name='dispatch')
# class GenreListView(View):
#     def get(self, request, *args, **kwargs):
#         genres = Genre.objects.all()
#         data = [{'id' : genre.id, 'name' : genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body.decode('utf-8'))
#         if data['name']:
#             new_genre = Genre(name=data['name'])
#             new_genre.save()
#             return JsonResponse({'id' : new_genre.id, 'name': new_genre.name}, status=201)
#         else:
#             return JsonResponse({'error' : 'bad request'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class GenreDetailView(View):
    def get(self, request, pk):
        try:
            genre = get_object_or_404(Genre, pk=pk)
            data = {'id' : genre.id, 'name' : genre.name}
            return JsonResponse(data)
        except Genre.DoesNotExist:
            return JsonResponse({'error' : 'id not found'}, status=404)
    def put(self, request, pk):
        try:
            genre = get_object_or_404(Genre, pk=pk)
            data = json.loads(request.body.decode('utf-8'))
            genre.name = data['name']
            genre.save()
            return JsonResponse({'id' : genre.id, 'name': genre.name}, status=200)
        except Genre.DoesNotExist:
            return JsonResponse({'error' : 'id not found'}, status=404)
    def delete(self, request, pk):
        try:
            genre = get_object_or_404(Genre, pk=pk)
            genre.delete()
            return JsonResponse({'message' : 'Gênero excluído com sucesso'}, status=404)
        except Genre.DoesNotExist:
            return JsonResponse({'error' : 'id not found'}, status=404)




