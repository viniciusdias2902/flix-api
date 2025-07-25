from django.shortcuts import render
from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer