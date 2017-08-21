from flask_restplus import Namespace
from flask_restplus import Resource, fields
from ..db.user_dao import get_all_user


users_ns = Namespace('users', description='Users related operations')

pagination = users_ns.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

user = users_ns.model('User', {
    'id': fields.String(required=False, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password'),
}, mask='{id, username}')

USERS = [
    {'id': 'felix', 'username': 'Felix', 'password':'hashpass'},
]

page_of_users = users_ns.inherit('Page of users', pagination, {
    'users': fields.List(fields.Nested(user))
})


@users_ns.route("/")
class UserList(Resource):
    @users_ns.doc('list_users')
    @users_ns.marshal_list_with(user)
    def get(self):
        return get_all_user()

