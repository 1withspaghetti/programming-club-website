from flask import Flask
from flask import request



app = Flask(__name__)

@app.route('/website/<long:post_id>')
def show_post(post_id) -> str:
    return f'Post {post_id}'

@app.route("/login", methods = ['HEAD'])
def login():
  pass

@app.route("/refresh", methods = ['HEAD'])
def refresh():
  pass

@app.route("/logout", methods = ['PATCH'])
def logout():
  pass

@app.route("/register", methods = ['POST'])
def register():
  pass

@app.route("/update/username", methods = ['PATCH'])
def update_username():
  pass

@app.route("/update/email", methods = ['PATCH'])
def update_email():
  pass

@app.route("/update/password", methods = ['PATCH'])
def update_email():
  pass

@app.route("/delete", methods = ['DELETE'])
def delete():
  pass


def get_id(reference):
  """ returns user id matching reference """
