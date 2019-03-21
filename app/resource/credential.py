from flask_restful import Resource, reqparse
from app.utils import LOG
from app.cmd.kafka import ConfigsCommand

kafka_configs = ConfigsCommand()
parser = reqparse.RequestParser(trim=True)
parser.add_argument('username', required=True, type=str, help='username cannot be blank')
parser.add_argument('password', required=True, type=str, help='password cannot be blank')

class User(Resource):

    def get(self, username=None):
        return {"response": "test"}

    def post(self):
        args = parser.parse_args()
        LOG.info('[request] username={username}'.format(username = args['username']))
        LOG.info('[request] password={password}'.format(password = args['password']))
        kafka_configs.create_user(args['username'], args['password'])