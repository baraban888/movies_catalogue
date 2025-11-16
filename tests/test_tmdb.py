from unittest.mock import Mock
from movies_catalogue import tmdb_client

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_single_movie_uses_correct_endpoint(monkeypatch):
    mock_movie = {"id": 1, "title": "Some movie"}
    called_urls = []

    def mock_get(url, headers):
        called_urls.append(url)
        return Mock(status_code=200, json=lambda: mock_movie)

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", mock_get)

    movie_id = 1
    movie = tmdb_client.get_single_movie(movie_id)

    expected_url = f"{tmdb_client.BASE_URL}/movie/{movie_id}"
    assert called_urls[0] == expected_url
    assert movie == mock_movie


def test_get_movie_images_uses_correct_endpoint(monkeypatch):
    # Підготовка фейкових даних
    mock_images = {
        "backdrops": [{"file_path": "/test-backdrop.jpg"}],
        "posters": [{"file_path": "/test-poster.jpg"}],
    }
    called_urls = []

    def mock_get(url, headers):
        # Запам’ятовуємо викликаний URL
        called_urls.append(url)
        # Повертаємо об'єкт, схожий на response
        return Mock(status_code=200, json=lambda: mock_images)

    # Підміняємо requests.get у tmdb_client
    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", mock_get)

    # Викликаємо функцію, яку тестуємо
    movie_id = 42
    images = tmdb_client.get_movie_images(movie_id)

    # 1) Перевіряємо правильність URL
    expected_url = f"{tmdb_client.BASE_URL}/movie/{movie_id}/images"
    assert called_urls[0] == expected_url

    # 2) Перевіряємо, що повернені дані — саме mock_images
    assert images == mock_images

def test_get_single_movie_cast_uses_correct_endpoint(monkeypatch):
    # Фейкові дані від API
    mock_data = {
        "cast": [
            {"name": "Actor 1"},
            {"name": "Actor 2"},
        ]
    }
    called_urls = []

    def mock_get(url, headers):
        # Запам’ятовуємо URL, який викликала функція
        called_urls.append(url)
        return Mock(status_code=200, json=lambda: mock_data)

    # Підміняємо requests.get у tmdb_client на mock_get
    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", mock_get)

    # Викликаємо тестовану функцію
    movie_id = 99
    cast = tmdb_client.get_single_movie_cast(movie_id)

    # 1) Перевірка правильного endpoint
    expected_url = f"{tmdb_client.BASE_URL}/movie/{movie_id}/credits"
    assert called_urls[0] == expected_url

    # 2) Перевірка правильних даних
    assert cast == mock_data["cast"]
