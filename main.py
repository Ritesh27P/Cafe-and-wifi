from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from random import choice
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    url = StringField('url', validators=[DataRequired()])
    wifi_rating= StringField('wifi_rating', validators=[DataRequired()])
    power = StringField('power', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])

    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '123456'
Bootstrap(app)


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
    coffee_qoute = ['Conscience keeps more people awake than coffee.', 'Decaffeinated coffee is like a hairless cat, it exists, but that doesn’t make it right.',
                    'People say money can’t buy happiness. They Lie. Money buys Coffee, Coffee makes Me Happy!', 'Good Coffee – Cheaper than Prozac!']
    cafes = Cafe.query.all()
    ran_qoute = choice(coffee_qoute)
    return render_template('index.html', cafes=cafes, quote=ran_qoute)


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_cafe = Cafe(
            name=request.form.get('name'),
            address=request.form.get('address'),
            url=request.form.get('url'),
            wifi_rating=request.form.get('wifi_rating'),
            power=request.form.get('power'),
            image=request.form.get('image')
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    pass

print(Cafe.query.all())
