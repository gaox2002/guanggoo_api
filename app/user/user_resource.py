from flask import abort, request
from flask_restplus import Namespace
from flask_restplus import Resource, fields

from app.db.user_models import User

user_ns = Namespace('user', description='Users related operations')

user = user_ns.model('User', {
    'id': fields.String(required=False, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password'),
}, mask='{id, username}')

USERS = [
    {'id': 'felix', 'username': 'Felix', 'password':'hashpass'},
]


@user_ns.route('/<id>')
class UserResource(Resource):
    @user_ns.doc("get_user")
    @user_ns.marshal_with(user)
    def get(self, id):
        for uo in USERS:
            if uo['id'] == id:
                return uo
        else:
            abort(404, 'No user found.')


@user_ns.route('')
class UserCreate(Resource):

    @user_ns.doc('create_user')
    @user_ns.expect(user)
    @user_ns.marshal_with(user, code=201)
    def post(self):
        data = request.json
        userCreated = User(id=data.get('id'), username = data.get('username'), password = data.get('password'))
        return userCreated, 201
