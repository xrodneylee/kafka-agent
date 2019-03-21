from flask_restful import Resource, reqparse
from app.utils import LOG
from app.cmd.kafka import TopicsCommand

kafka_topics = TopicsCommand()

class Topic(Resource):

    def get(self):
        response = kafka_topics.list_topic()
        return response