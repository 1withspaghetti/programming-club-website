from os.path import isfile, join
from os import listdir
from unittest import TestCase
from flask import Flask, url_for
from auth import routing
import sqlalchemy
from flask_bcrypt import Bcrypt
from auth.models import User

#generate absolute paths for static pages
def get_and_index_static_file_urls() -> list:
    files = [file for file in listdir('static') if isfile(join(url_for('static', file)))]
    return files


app = Flask(__name__)
db = sqlalchemy(app)
bcrypt = Bcrypt(app)

app.register_blueprint(routing.bp)








