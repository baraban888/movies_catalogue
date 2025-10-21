import os
import requests
from dotenv import load_dotenv
import random

load_dotenv()
API_TOKEN = os.getenv("TMDB_API_TOKEN")

BASE_URL = "https://api.themoviedb.org/3"

def _headers():
    if not API_TOKEN:
        raise RuntimeError("TMDB_API_TOKEN is not set")
    return {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }

def get_movies(list_type="popular", language="pl-PL", page=1):
    url = f"{BASE_URL}/movie/{list_type}"
    resp = requests.get(url, headers=_headers(), params={"language": language, "page": page}, timeout=10)
    resp.raise_for_status()
    return resp.json()["results"]

def get_random_movies(how_many=8, list_type="popular", language="pl-PL", page=1):
    movies = get_movies(list_type=list_type, language=language, page=page)  # это уже список!
    random.shuffle(movies)
    return movies[:how_many]

def get_movie_details(movie_id, language="pl-PL"):
    url = f"{BASE_URL}/movie/{movie_id}"
    resp = requests.get(url, headers=_headers(), params={"language": language}, timeout=10)
    resp.raise_for_status()
    return resp.json()

def search_movie(query, language="pl-PL", page=1):
    url = f"{BASE_URL}/search/movie"
    resp = requests.get(url, headers=_headers(),
                        params={"query": query, "language": language, "page": page, "include_adult": "false"},
                        timeout=10)
    resp.raise_for_status()
    return resp.json()["results"]

def get_poster_url(path, size="w500"):
    if not path:
        return ""
    return f"https://image.tmdb.org/t/p/{size}{path}"
