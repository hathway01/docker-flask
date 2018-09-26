from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, PasswordField, validators

from .models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, message="Name should be 4 character long")])
    email = StringField('Email Address', [validators.Length(min=6, message="Email should be 6 character long")])
    password = PasswordField('Password', [validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign Up")


    def validate(self):
        if not FlaskForm.validate(self):
            return False
        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken.Try signing in or use diffrent mail id")
            return False
        else:
            return True


class SearchForm(FlaskForm):
    text = StringField("text")
    submit = SubmitField("Search")


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email,password=password).first()
        if user:
            return True
        else:
            self.email.errors.append("E-mail/Password is not correct")
            return False


class BlogForm(FlaskForm):
    title = StringField(" Title ",[validators.DataRequired()])
    content = TextAreaField("Blog Content",[validators.DataRequired()])
    submit = SubmitField("Publish")

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        else:
            return True
