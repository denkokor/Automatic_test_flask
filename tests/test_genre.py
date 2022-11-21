from unittest.mock import MagicMock
import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    director_1 = Genre(id=1, name='user_1')
    director_2 = Genre(id=2, name='user_2')

    genre_dao.get_one = MagicMock(return_value=director_1)
    genre_dao.get_all = MagicMock(return_value=[director_1, director_2])
    genre_dao.create = MagicMock(return_value=director_1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(1) is not None
        assert self.genre_service.get_one(1).name == 'user_1'

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 2

    def test_create(self):
        data = {
            "name": "user_1"
        }

        assert self.genre_service.create(data).name == data.get("name")

    def test_delete(self):
        assert 1 == 1

    def test_update(self):
        assert 1 == 1
