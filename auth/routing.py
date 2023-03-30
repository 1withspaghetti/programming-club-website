from flask import Flask
from flask import request
<<<<<<< HEAD
from flask import render_template
from app import app
from actions import actions

class routing():

    @app.route("/test")
    def test_print():
        return f'LHS Programming club website!'

    @app.route("/login", methods = ['HEAD', 'POST'])
    def login():
        if request.method == 'POST':
            if actions.valid_login(request.form['username'], request.form['password']):
                actions.login_user(request.form['username'])
            else:
                error = 'invalid credentials'
                render_template('invalid_credentials.html')
        render_template('login.html', error)
        

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
    def update_password():
        pass

    @app.route("/delete", methods = ['DELETE'])
    def delete():
        pass


    def get_id(reference):
        """ returns user id matching reference """
=======



app = Flask(__name__)



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
def update_password():
  pass

@app.route("/delete", methods = ['DELETE'])
def delete():
  pass


def get_id(reference):
  """ returns user id matching reference """
>>>>>>> 12852cf3385c7f5e792b28205df4d45bd53bbc9d
