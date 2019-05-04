from flask_wtf import FlaskForm
from wtforms import Form, StringField


class MovieSearchForm(FlaskForm):
    search = StringField(render_kw={"placeholder": "Search movie"})
