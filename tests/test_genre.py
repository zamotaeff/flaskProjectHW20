import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def test_genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.name == 'genre1'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_data = {'name': 'Name'}
        new_genre = self.genre_service.create(genre_data)
        assert new_genre.id is not None

    def test_update(self):
        self.genre_service.update(1)

    def test_delete(self):
        result = self.genre_service.delete(1)
        assert result is None