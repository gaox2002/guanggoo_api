from ..user_models import User
from .. import jwt
import hashlib
import re


class UserInfo(object):
    """Object to carry information in jwt token"""
    def __init__(self, id, username, guid):
        self.id = id
        self.username = username
        self.guid = guid


@jwt.authentication_handler
def authenticate(username, password):
    if re.match(r"[^@]+@[^@]+\.[^@]+", username):
        user = User.query.filter_by(email=username).first()
    else:
        user = User.query.filter_by(username=username)
    if user and user.password == hashlib.sha1(password).hexdigest():
        return user

@jwt.identity_handler
def identity(payload):
    user_id = payload['identity']
    user = User.get(user_id, None)
    return UserInfo(id = user.id, username = user.username, guid = user.guid)

