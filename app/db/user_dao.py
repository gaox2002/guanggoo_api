from . import db
from .user_models import User


def create_user(user):
    db.session.add(user)
    db.session.commit()


def get_user(id):
    return User.query.get(id)


def get_all_user():
    return User.query.all()


def update_user(db_user, req_user):
    if req_user.get('email') is not None:
        db_user.email = req_user.get('email')
    if req_user.get('password') is not None:
        db_user.password = req_user.get('password')

    db.session.add(db_user)
    db.commit()
