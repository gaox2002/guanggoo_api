from flask_restplus import Namespace
from flask_restplus import Resource, fields

question_ns = Namespace('question', description='Challenge question operations')

question = question_ns.model('Question', {
    'id': fields.String(required=False, description='The user identifier'),
    'question_key': fields.String(required=True, description='The username to login'),
    'user_id': fields.String(required=True, description='user nickname shows on the page'),
    'answer': fields.String(required=True, description='The email'),
})


@question_ns.route('/<id>')
class Question(Resource):
    pass

