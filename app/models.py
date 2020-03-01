from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    point_total = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Airport(db.Model):
    Airport_Name = db.Column(db.String(3), primary_key=True)
    Description = db.Column(db.String)
    IATA = db.Column(db.String)

    def __repr__(self):
        return '<Airport {}>'.format(self.Airport_Name)
