from flask import request, render_template, Blueprint
from accounts import accounts

bp = Blueprint('auth', __name__)

@bp.route("/")
def test_print():
        return f'LHS Programming club website!'

@bp.route("/login", methods = ['HEAD', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            ''''send refresh jwt to client'''
        else:
            error = 'invalid credentials'
            render_template('invalid_credentials.html')
    render_template('login.html', error)


@bp.route("/refresh", methods = ['HEAD'])
def refresh():
    if request.method == 'HEAD':
        valid_login()

@bp.route("/logout", methods = ['PATCH'])
@accounts.login_dependent
def logout():
    pass

@bp.route("/register", methods = ['HEAD'])
def register():
    pass



@bp.route("/update/username", methods = ['PATCH'])
@accounts.login_dependent
def update_username():
    pass

@bp.route("/update/email", methods = ['PATCH'])
@accounts.login_dependent
def update_email():
    pass

@bp.route("/update/password", methods = ['PATCH'])
@accounts.login_dependent
def update_password():
    pass

@bp.route("/delete", methods = ['DELETE'])
@accounts.login_dependent
def delete():
    pass


def valid_login(username, password):
        if username != None and password != None:
            return True
        return False
