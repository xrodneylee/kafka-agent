from flask_restful import Resource, reqparse
from app.utils import LOG
from app.cmd.kafka import AclsCommand

kafka_acls = AclsCommand()
parser = reqparse.RequestParser(trim=True)
parser.add_argument('username', required=True, type=str, help='username cannot be blank')
parser.add_argument('topic', required=True, type=str, help='topic cannot be blank')
parser.add_argument('role', required=True, type=str, help='role(producer/consumer) cannot be blank')

class ACL(Resource):
    
    def post(self):
        args = parser.parse_args()
        LOG.info('[request] username={username}'.format(username = args['username']))
        LOG.info('[request] topic={topic}'.format(topic = args['topic']))
        LOG.info('[request] role={role}'.format(role = args['role']))

        if args['role'] == 'producer':
            response = kafka_acls.create_producer_acl(args['username'], args['topic'])
        elif args['role'] == 'consumer':
            response = kafka_acls.create_consumer_acl(args['username'], args['topic'])
        else:
            response = 'invalid role'

        return response