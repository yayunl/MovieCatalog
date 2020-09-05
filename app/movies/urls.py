# app/movies/urls.py

from django.urls import path

from .views import MovieListView, MovieDetailView


urlpatterns = [
    path("api/movies/", MovieListView.as_view()), # list view
    path("api/movies/<int:pk>/", MovieDetailView.as_view()) # detail view
]