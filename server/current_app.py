from app import app
from flask import request

request_context = app.test_request_context()
request_context.push()