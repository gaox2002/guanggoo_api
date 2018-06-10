from flask_restplus import Namespace, fields, Resource, abort

from ..user_models import User
from flask_jwt_extended import create_access_token
import hashlib
import re


class LogUser(object):
    """Object to carry login credential"""
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserInfo(object):
    """Object to carry information in jwt token"""
    def __init__(self, id, username, guid):
        self.id = id
        self.username = username
        self.guid = guid


token_ns = Namespace('auth', description='Users related operations')

token = token_ns.model('A token for user', {
    'access_token': fields.Integer(description='access token')
})

login_user = token_ns.model('user login information', {
    'username': fields.String(description='login username'),
    'password': fields.String(description='login password')
})


@token_ns.route("/login")
class Login(Resource):
    @token_ns.doc('login')
    @token_ns.expect(login_user)
    @token_ns.marshal_with(token_ns)
    def post(self):
        username = login_user.username
        password = login_user.password
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            user = User.query.filter_by(email=username).first()
        else:
            user = User.query.filter_by(username=username)

        if not user:
            abort(400, "can not find the username")

        if user.password != hashlib.sha1(password).hexdigest():
            abort(400, "password is not valid")

        user_info = UserInfo(user.id, user.username, user.guid)
        access_token = create_access_token(user_info)

        return access_token
