# WTF uses a class to represent a traditional form.
# The class LoginForm describes the fields of our form. Note; we're
# paying no attention to the appearance of the form just yet.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# DataRequired ensures that a user has inputted data into the field.
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
