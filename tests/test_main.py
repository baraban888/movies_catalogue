from movies_catalogue.main import app
from unittest.mock import Mock
import pytest


@pytest.mark.parametrize("list_type", ["popular", "top_rated", "upcoming", "now_playing"])
def test_homepage_uses_correct_list_type(monkeypatch, list_type):
    # Фейкові дані від API
    api_mock = Mock(return_value=[])

    # Підміняємо get_movies_list у tmdb_client на наш mock
    monkeypatch.setattr("movies_catalogue.tmdb_client.get_movies_list", api_mock)

    with app.test_client() as client:
        # Якщо popular — перевіряємо дефолтний варіант без параметра
        if list_type == "popular":
            response = client.get("/")
        else:
            # Для інших списків додаємо ?list_type=...
            response = client.get(f"/?list_type={list_type}")

        # Перевіряємо, що сторінка відкрилася
        assert response.status_code == 200

    # 🧠 У твому коді get_movies_list(list_type) викликається ПОЗИЦІЙНО,
    # тому ми перевіряємо саме позиційний аргумент, а не keyword
    api_mock.assert_called_once_with(list_type)


def test_homepage_invalid_list_type_falls_back_to_popular(monkeypatch):
    api_mock = Mock(return_value=[])
    monkeypatch.setattr("movies_catalogue.tmdb_client.get_movies_list", api_mock)

    with app.test_client() as client:
        response = client.get("/?list_type=invalid_value")
        assert response.status_code == 200

    # Якщо list_type не з MOVIE_LISTS — має використатися 'popular'
    api_mock.assert_called_once_with("popular")
