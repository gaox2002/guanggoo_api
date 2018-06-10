from flask_restplus import Namespace
from flask_restplus import Resource, fields
from flask_jwt_extended import jwt_required, jwt_optional
from .. import api
from .topic_models import Topic


topic_ns = Namespace('topics', description='Topic related operations')

topic = topic_ns.model('topic', {
    'id': fields.String(required=False, description='The topic identifier'),
    'title': fields.String(required=True, description='The topicname'),
    'content': fields.String(required=True, description='The topic password'),
})

# dummy data
TOPICS = [
    {'id': 'topic-id', 'title': 'This is topic', 'content':'Topic content'},
]


@topic_ns.route("/")
class TopicList(Resource):
    @topic_ns.doc('list_topics')
    @topic_ns.marshal_list_with(topic)
    @jwt_optional
    def get(self):
        return Topic.query.order_by(Topic.update_time.desc()).limit(50).all()

    @topic_ns.doc('topic')
    @topic_ns.marshal(topic)
    @jwt_required
    def post(self):
        pass


@topic_ns.route('/<int:id>')
@topic_ns.response(404, 'Todo not found')
@topic_ns.param('id', 'The task identifier')
class TopicResource(Resource):
    '''Show a single todo item and lets you delete them'''
    @topic_ns.doc('get_topic')
    @topic_ns.marshal_with(topic)
    def get(self, id):
        '''Fetch a given resource'''
        return Topic.get(id)

    @topic_ns.doc('delete_topic')
    @topic_ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        Topic.delete(id)
        return '', 204

    @topic_ns.doc('update_topic')
    @topic_ns.expect(topic)
    @topic_ns.marshal_with(topic)
    def put(self, id):
        '''Update a task given its identifier'''
        return Topic.update(id, api.payload)
