# app/movies/serializers.py

# What is serializer?
# Serializers deserialize data from HTTP Post/PUT request payload, validate it, and convert it into
# something Django can work with. On the other way, when HTTP GET request is received, serializers
# serialize data from db into JSON to be sent back with HTTP response.
# END

from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)