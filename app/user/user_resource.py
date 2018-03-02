from flask import abort, request
from flask_restplus import Namespace
from flask_restplus import Resource, fields

import uuid

from app.user.user_dao import create_user, get_user
from app.user_models import User

user_ns = Namespace('user', description='Users related operations')

user = user_ns.model('User', {
    'id': fields.String(required=False, description='The user identifier'),
    'username': fields.String(required=True, description='The username to login'),
    'nickname': fields.String(required=False, description='user nickname shows on the page'),
    'email': fields.String(required=True, description='The email'),
    'password': fields.String(required=True, description='The user password'),
    'password_confirm': fields.String(required=True, description='Confirm user password again'),
})


@user_ns.route('/<id>')
class UserResource(Resource):
    @user_ns.doc("get_user")
    @user_ns.marshal_with(user, mask='id, username, nickname, email')
    def get(self, id):
        quser = get_user(id)
        if quser:
            return quser
        else:
            abort(404, 'No user found')

    @user_ns.doc("update_user")
    @user_ns.expect(user)
    @user_ns.marshal_with(user)
    def put(self, id):
        quser = get_user(id)
        if quser:
            data = request.json

            return None, 204
        else:
            abort(404, 'No user found')


@user_ns.route('')
class UserCreate(Resource):

    @user_ns.doc('create_user')
    @user_ns.expect(user, validate=True)
    @user_ns.marshal_with(user, code=201)
    def post(self):
        data = request.json
        # profile = Profile(id=uuid.uuid4().hex, email=data.get('email'))
        if data.get('password') != data.get('password_confirm'):
            abort(400, 'Passsword not match')

        nickname = data.get('nickname')
        if nickname is None:
            nickname = data.get('username')

        userCreated = User(id=uuid.uuid4().hex, username = data.get('username'), email = data.get('email'),
                           nickname = nickname, password = data.get('password'))
        create_user(userCreated)
        return userCreated, 201
