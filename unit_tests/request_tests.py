from flask import request
from app import app

with app.test_request_context("/login", method = 'POST'):
    assert request.method == 'POST'

