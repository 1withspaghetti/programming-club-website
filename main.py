from os.path import isfile, join
from os import listdir
from flask import Flask, url_for, render_template
from unittest import TestCase
from auth import routing
import sqlalchemy
from flask_bcrypt import Bcrypt
from auth.models import User

#generate absolute paths for static pages
def get_and_index_static_file_urls() -> list:
  files = [file for file in listdir('static') if isfile(join(url_for('static', file)))]
  return files

if __name__ == "__main__":
  app.run()

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/register")
def register():
  return render_template("register.html")

app = Flask(__name__)
db = sqlalchemy(app)
bcrypt = Bcrypt(app)
