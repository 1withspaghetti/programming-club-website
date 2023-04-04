from flask import request, Flask

app = Flask(__name__)

with app.test_request_context("/login", method = 'POST'):
    assert request.method == 'POST'

