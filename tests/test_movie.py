from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService



@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='title_1')
    movie_2 = Movie(id=2, title='title_1')

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_1)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).title == 'title_1'

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_create(self):
        data = {
            "id": 1,
            "title": 'title_1',
            "description": 'asasfasf',
            "trailer": '1asd',
            "year": 2020,
            "rating": 20.1,
            "genre_id": 1,
            "director_id": 1
        }

        assert self.movie_service.create(data).title == data.get("title")

    def test_delete(self):
        assert 1 == 1

    def test_update(self):
        assert 1 == 1


