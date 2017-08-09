from flask import abort, request
from flask_restplus import Namespace
from flask_restplus import Resource, fields

from app.db.user_models import User

users_ns = Namespace('users', description='Users related operations')

user = users_ns.model('User', {
    'id': fields.String(required=False, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password'),
}, mask='{id, username}')

USERS = [
    {'id': 'felix', 'username': 'Felix', 'password':'hashpass'},
]


@users_ns.route("/")
class UserList(Resource):
    @users_ns.doc('list_users')
    @users_ns.marshal_list_with(user)
    def get(self):
        return USERS

