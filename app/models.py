from app import db

class User(db.Model):
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
    def __repr__(self):
        return '<Airport {}>'.format(self.Airport_Name)  