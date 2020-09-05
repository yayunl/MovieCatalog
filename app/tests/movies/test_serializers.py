# app/tests/movies/test_serializers.py
from movies.serializers import MovieSerializer


def test_valid_movie_serializer():
    valid_ser_data ={
        "title": "Raising Arizona",
        "genre": "comedy",
        "year": "1987"
    }
    ser = MovieSerializer(data=valid_ser_data)
    assert ser.is_valid()
    assert ser.validated_data == valid_ser_data
    assert ser.data == valid_ser_data
    assert ser.errors == dict()


def test_invalid_movie_serializer():
    invalid_ser_data = {
        "title": "Raising Arizona",
        "genre": "comedy",
    }
    ser = MovieSerializer(data=invalid_ser_data)
    assert not ser.is_valid()
    assert ser.validated_data == dict()
    assert ser.data == invalid_ser_data
    assert ser.errors == {"year": ["This field is required."]}