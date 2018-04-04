from . import db
from flask_security import UserMixin, RoleMixin


roles_users = db.Table('roles_users',
        db.Column('user_id', db.String(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(128), primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True)
    nickname = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(128))
    guid = db.Column(db.String(256), unique=True, index=True)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    profile_id = db.Column(
        db.String(64), db.ForeignKey('profile.id', ondelete='CASCADE')
    )
    profile = db.relationship('Profile', backref = 'user', lazy='joined')


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


# information about user
class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.String(64), primary_key=True)
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(1))

