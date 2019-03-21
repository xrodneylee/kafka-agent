from flask_restful import Resource, reqparse
from app.utils import LOG
from app.cmd.kafka import TopicsCommand

kafka_topics = TopicsCommand()

parser = reqparse.RequestParser(trim=True)
parser.add_argument('topic', required=True, type=str, help='topic cannot be blank')
parser.add_argument('replication', required=True, type=str, help='replication cannot be blank')
parser.add_argument('partitions', required=True, type=str, help='partitions cannot be blank')

class Topic(Resource):

    def get(self):
        response = kafka_topics.list_topic()
        return response

    def post(self):
        args = parser.parse_args()
        LOG.info('[request] topic={topic}'.format(topic = args['topic']))
        LOG.info('[request] replication={replication}'.format(replication = args['replication']))
        LOG.info('[request] partitions={partitions}'.format(partitions = args['partitions']))
        response = kafka_topics.create_topic(args['topic'], args['replication'], args['partitions'])
        return response