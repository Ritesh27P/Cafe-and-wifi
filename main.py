from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(200), unique=True, nullable=True)
    wifi_rating = db.Column(db.String(20), unique=False, nullable=False)
    power = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(20), unique=False, nullable=False)


@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)


@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
    pass

