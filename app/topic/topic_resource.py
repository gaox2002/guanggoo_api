from flask import abort, request
from flask_restplus import Namespace
from flask_restplus import Resource, fields

from app.db.topic_models import Topic, Comment

topic_ns = Namespace('topics', description='Topic related operations')

topic = topic_ns.model('topic', {
    'id': fields.String(required=False, description='The topic identifier'),
    'title': fields.String(required=True, description='The topicname'),
    'content': fields.String(required=True, description='The topic password'),
})

TOPICS = [
    {'id': 'topic-id', 'title': 'This is topic', 'content':'Topic content'},
]


@topic_ns.route("/")
class TopicList(Resource):
    @topic_ns.doc('list_topics')
    @topic_ns.marshal_list_with(topic)
    def get(self):
        return TOPICS
