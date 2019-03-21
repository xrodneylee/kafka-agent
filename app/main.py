from flask import Flask
from flask_restful import Api
from app.resource.credential import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response