import os
import requests,random
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.themoviedb.org/3"
API_KEY   = os.getenv("TMDB_API_KEY")
API_TOKEN = os.getenv("TMDB_API_TOKEN")
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

def get_single_movie(movie_id):
    endpoint = f"{BASE_URL}/movie/{movie_id}"
    headers = _headers()
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movie_credits(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    resp = requests.get(url, headers=_headers())
    resp.raise_for_status()
    return resp.json()

def get_movie_images(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/images"
    resp = requests.get(url, headers=_headers())
    resp.raise_for_status()
    return resp.json()

def get_movies_list(list_name):
    endpoint = f"{BASE_URL}/movie/{list_name}"
    headers = _headers()
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["results"]

def get_random_backdrop(movie_id):
    images = get_movie_images(movie_id)
    backdrops = images.get("backdrops")
    if not backdrops:
        return None
    chosen = random.choice(backdrops)
    return f"https://image.tmdb.org/t/p/w780{chosen['file_path']}"

def get_poster_url(path, size="w500"):
    if not path:
        return "https://via.placeholder.com/500x750?text=No+Image"
    return f"https://image.tmdb.org/t/p/{size}{path}"

def get_profile_url(path, size="w185"):
    if not path:
        return ""          # можно вернуть placeholder, если хочешь
    return f"https://image.tmdb.org/t/p/{size}{path}"

def get_tv_today():
    endpoint = f"{BASE_URL}/tv/airing_today"
    params = {"api_key": API_KEY}
    resp = requests.get(endpoint, params=params)
    resp.raise_for_status()
    return resp.json()["results"]
