import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def test_movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.title == 'title 1'

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_create(self):
        movie_data = {'name': 'Name'}
        new_movie = self.movie_service.create(movie_data)
        assert new_movie.id is not None
        assert new_movie.title == 'title 1'
        assert new_movie.year == 2001
        assert new_movie.description == 'desk1'

    def test_update(self):
        self.movie_service.update(1)

    def test_delete(self):
        result = self.movie_service.delete(1)
        assert result is None