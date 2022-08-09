import pytest
from unittest.mock import MagicMock

from dao.genre import GenreDAO
from dao.model.genre import Genre
from dao.director import DirectorDAO
from dao.model.director import Director
from dao.movie import MovieDAO
from dao.model.movie import Movie


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    test1 = Genre(id=1, name='genre1')
    test2 = Genre(id=2, name='genre2')
    test3 = Genre(id=3, name='genre3')

    genre_dao.query = MagicMock()
    genre_dao.get_one = MagicMock(return_value=test1)
    genre_dao.get_all = MagicMock(return_value=[test1, test2, test3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    test1 = Director(id=1, name='dir1')
    test2 = Director(id=2, name='dir2')
    test3 = Director(id=3, name='dir3')

    director_dao.query = MagicMock()
    director_dao.get_one = MagicMock(return_value=test1)
    director_dao.get_all = MagicMock(return_value=[test1, test2, test3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    test1 = Movie(id=1, title='title 1', description='desk1', year=2001)
    test2 = Movie(id=2, title='title 22', description='desk2', year=2002)

    movie_dao.query = MagicMock()
    movie_dao.get_one = MagicMock(return_value=test1)
    movie_dao.get_all = MagicMock(return_value=[test1, test2])
    movie_dao.create = MagicMock(return_value=test1)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao