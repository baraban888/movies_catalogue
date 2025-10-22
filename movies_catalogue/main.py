from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

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

if __name__ == "__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["TRAP_HTTP_EXCEPTIONS"] = True
    app.config["DEBUG"] = True
    app.run(debug=True)

