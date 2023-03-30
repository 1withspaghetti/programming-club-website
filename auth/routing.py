from flask import Flask
from flask import request
from flask import url_for
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route('/website/<long:post_id>')
def show_post(post_id) -> str:
    return f'Post {post_id}'

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return make_post()
    else:
        return make_get()

def make_post():
    'post request'

def make_get():
    'shows login screen'

'this could be potentially put somewhere else'
def get_and_index_static_file_urls() -> list:
    files = [file for file in listdir('static') if isfile(join(url_for('static', file)))]
    return files
