from flask_restful import Resource, reqparse
from app.utils import LOG
from app.cmd.kafka import ConfigsCommand

kafka_configs = ConfigsCommand()
parser = reqparse.RequestParser(trim=True)
parser.add_argument('username', required=True, type=str, help='username cannot be blank')
parser.add_argument('password', required=True, type=str, help='password cannot be blank')

class User(Resource):

    def get(self, username=None):
        if username:
            response = kafka_configs.get_user(username)
        else:
            response = kafka_configs.list_user()
        return response

    def post(self):
        args = parser.parse_args()
        LOG.info('[request] username={username}'.format(username = args['username']))
        LOG.info('[request] password={password}'.format(password = args['password']))
        response = kafka_configs.create_user(args['username'], args['password'])
        return response