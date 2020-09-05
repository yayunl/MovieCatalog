import json, pytest
from movies.models import Movie


# Test add movies
@pytest.mark.django_db
def test_add_movie(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        '/api/movies/',
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )

    assert resp.status_code == 201
    assert resp.data['title'] == 'The Big Lebowski'

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        '/api/movies/',
        {}, # empty payload
        content_type="application/json"
    )

    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        '/api/movies/',
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        }, # Missing keys
        content_type="application/json"
    )

    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


# Test get movies
@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    resp = client.get(f"/api/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    movie_2 = add_movie("No Country for Old Men", "thriller", "2007")
    resp = client.get(f"/api/movies/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == movie.title
    assert resp.data[1]["title"] == movie_2.title


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/movies/foo/")
    assert resp.status_code == 404

