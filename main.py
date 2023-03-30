from os.path import isfile, join
from os import listdir
from flask import Flask, url_for
from auth.routing import routing
from app import app


router = routing()

#generate absolute paths for static pages
def get_and_index_static_file_urls() -> list:
    files = [file for file in listdir('static') if isfile(join(url_for('static', file)))]
    return files

if __name__ == "__main__":
    app.run()
