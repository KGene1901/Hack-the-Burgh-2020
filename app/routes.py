from flask import Flask
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, LoginManager
from flask_login import LoginManager

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'h'
login = LoginManager(app)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}
    Airport_Name = db.Column(db.String(3), primary_key=True)
    Description = db.Column(db.String)
    IATA = db.Column(db.String)

    def __repr__(self):
        return '<Airport {}>'.format(self.Airport_Name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route("/")
@app.route('/index')
def hell():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
