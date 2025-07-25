from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    attempts = db.relationship('Attempt', backref='user', lazy='dynamic')

    @property
    def best_score(self):
        best = self.attempts.order_by(Attempt.score.desc()).first()
        return best.score if best else 0

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    choices = db.Column(db.PickleType, nullable=False)  # {'A':'...','B':'...'}
    correct = db.Column(db.String(1), nullable=False)
