import json
from flask import request

from flaskcinema import app
# from flaskcinema.forms import MovieSearchForm
from flaskcinema.utils import get_result_from_api
from flaskcinema.models import Rating

ratings = []

@app.route("/", methods=['GET'])
def homepage():
    print("Redirect home is called")
    movies = []
    return render_template('index.html')

@app.route("/search", methods=["GET"])
def search_movies_by_name():
    movie_title = request.args.get('movie_title')
    movies = []

    # "s" return a dict of all search movies with key "Search"
    result = get_result_from_api(movie_title, "s")
    if result:
        movies = result

    return json.dumps({"result: ": movies})


@app.route("/title", methods=["GET"])
def get_movie():
    movie_id = request.args.get('movie_id')
    movie = {}

    # "i" return a dict of movie
    result = get_result_from_api(movie_id, "i")
    if result:
        movie = result

    return json.dumps({"result: ": movie})


@app.route("/rating", methods=["GET"])
def get_rating():
    movie_id = request.args.get('movie_id')
    user_id = request.args.get('user_id')

    ratings = []
    result = select_all(movie_id, user_id, column="ratings")
    if result:
        ratings = result

    return json.dumps({"result: ": ratings})


@app.route("/rating", methods=["POST"])
def rate_movie():
    user_id = request.args.get('user_id')
    movie_id = request.args.get('movie_id')
    score = request.args.get('score')

    rating1 = Rating(movie_id=movie_id, user_id=user_id, score=score)
    insert(rating1)

    return json.dumps({"result": ratings})


def select_all(movie_id, user_id, column="ratings"):
    rating1 = Rating(movie_id="tt1375666", user_id="user1", score=2)
    rating2 = Rating(movie_id="tt1790736", user_id="quang", score=4)
    ratings.append(rating1.__dict__)
    ratings.append(rating2.__dict__)
    return ratings


def insert(rating):
    ratings.append(rating.__dict__)


# @app.route("/", methods=['GET', 'POST'])
# def homepage():
#     print("Redirect home is called")
#     movies = []
#     form = MovieSearchForm()
#     if form.validate_on_submit():
#         if form.search.data == "":
#             movies = []
#             return redirect(url_for('homepage'))
#         movie_title = form.search.data
#         movies = search_movies_by_name(movie_title)
#     return render_template('home.html', title="Home", form=form,
#                            movies=movies, ratings=ratings)


# @app.route("/title", methods=["GET", "POST"])
# def moviepage():
#     movie_id = request.args.get('movie_id')
#     movie = get_movie_by_id(movie_id)
#     return render_template('movie.html', title="Detail", movie=movie)
