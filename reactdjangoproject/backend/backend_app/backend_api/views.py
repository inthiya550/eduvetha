from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets
# Create your views here.

class MovieViewset(viewsets.ModelViewSet):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()
