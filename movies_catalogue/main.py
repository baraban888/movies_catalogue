import os
from pathlib import Path
from flask import Flask, render_template, request
import tmdb_client

BASE_DIR = Path(__file__).parent.resolve()

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
print("CWD:         ", os.getcwd())
print("ROOT_PATH:   ", app.root_path)
print("TEMPLATES:   ", app.jinja_loader.searchpath)

FAVORITES = set()

MOVIE_LISTS = {"popular": "Popular",
             "top_rated": "Top Rated",
             "upcoming": "Upcoming",
             "now_playing": "Now Playing"}

@app.route("/")
def homepage():
    list_type = request.args.get("list_type", "popular")
    if list_type not in MOVIE_LISTS:
        list_type = "popular"
    movies = tmdb_client.get_movies_list(list_type)
    return render_template(
        "homepage.html",
        movies=movies,
        current_list=list_type,
        movie_lists=MOVIE_LISTS,
        get_poster=tmdb_client.get_poster_url
    )

@app.route("/add_to_favorites", methods=["POST"])
def add_to_favorites():
    movie_id = request.form.get("movie_id")
    if movie_id:
        FAVORITES.add(movie_id)
    return "", 204  # відповідаємо без перезавантаження сторінки

@app.route("/favorites")
def favorites():
    from tmdb_client import get_movie_details
    movies = [get_movie_details(movie_id) for movie_id in FAVORITES]
    return render_template("favorites.html", movies=movies, get_poster=tmdb_client.get_poster_url)

@app.context_processor
def inject_active_page():
    return {"active_page": request.endpoint}

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    credits = tmdb_client.get_movie_credits(movie_id)
    cast = [c for c in credits.get("cast", []) if c.get("profile_path")][:8]
    backdrop = tmdb_client.get_random_backdrop(movie_id)
    return render_template(
        "movie_details.html",
        movie=movie,
        cast=cast,
        backdrop=backdrop,
        get_poster=tmdb_client.get_poster_url,
        get_profile=tmdb_client.get_profile_url
    )

@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    results = tmdb_client.search_movie(q) if q else []
    return render_template("search.html", q=q, results=results, get_poster=tmdb_client.get_poster_url)

@app.route("/tv_today")
def tv_today():
    try:
        tv_shows = tmdb_client.get_tv_today()
    except Exception as e:
        print(f"Error fetching TV shows airing today: {e}")
        tv_shows = []   
    return render_template("tv_today.html", tv_shows=tv_shows,get_poster=tmdb_client.get_poster_url)

@app.context_processor
def inject_active_page():
    return {"active_page": request.endpoint}

if __name__ == "__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["TRAP_HTTP_EXCEPTIONS"] = True
    app.config["DEBUG"] = True
    app.run(debug=True)

