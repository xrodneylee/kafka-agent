from flask import Flask
from flask_restful import Api
from app.resource.credential import User
from app.resource.acl import ACL
from app.resource.topic import Topic

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users', '/users/<username>')
api.add_resource(ACL, '/acls')
api.add_resource(Topic, '/topics')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response