from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

@app.route("/")
def homepage():
    list_type = request.args.get("list_type", "popular")  # popular | top_rated | upcoming | now_playing
    movies = tmdb_client.get_movies(list_type=list_type)
    return render_template("homepage.html", movies=movies, list_type=list_type, get_poster=tmdb_client.get_poster_url)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_movie_details(movie_id)
    return render_template("movie.html", movie=movie, get_poster=tmdb_client.get_poster_url)

@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    results = tmdb_client.search_movie(q) if q else []
    return render_template("search.html", q=q, results=results, get_poster=tmdb_client.get_poster_url)

if __name__ == "__main__":
    app.run(debug=True)

