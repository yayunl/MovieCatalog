# app/movies/views.py

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


class MovieListView(APIView):
    """
    A List view of movies.
    """
    def post(self, request, format=None):
        # Serialize the http post payload
        ser = MovieSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        movies = Movie.objects.all()
        ser = MovieSerializer(movies, many=True) # serialize the query to json
        return Response(ser.data)


class MovieDetailView(APIView):
    """
    A Detail view of a specific movie with given pk/slug.
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        ser = MovieSerializer(movie) # Serialize a single instance to json
        return Response(ser.data)
