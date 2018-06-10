from flask import Flask, Blueprint
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security

from app.user_models import User, Role
from .auth.jwt import token_ns
from .user.user_resource import user_ns
from .user.users_resource import users_ns
from .topic.topic_resource import topic_ns
from .config import config
from flask_restplus import Api
from flask_jwt_extended import JWTManager


api = Api(version='1.0', title='guanggoo API',
          description='APIs for guanggoo CMS')


mail = Mail()
db = SQLAlchemy()
moment = Moment()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(token_ns)
    api.add_namespace(user_ns)
    api.add_namespace(users_ns)
    api.add_namespace(topic_ns)
    app.register_blueprint(blueprint)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    return app
