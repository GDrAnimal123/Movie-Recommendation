from flask import Flask, render_template, url_for
from flask_jsglue import JSGlue

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# jsglue = JSGlue(app)
jsglue = JSGlue()
jsglue.init_app(app)

from flaskcinema import routes
