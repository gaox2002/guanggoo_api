from .. import db
from datetime import datetime


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.String(128), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.String(128), db.ForeignKey('user.id'), nullable=False)

    db.relationship('Comment', backref='topic', order_by='Comment.create_time')


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.String(128), primary_key=True)
    topic_id = db.Column(db.String(128), db.ForeignKey('topic.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

