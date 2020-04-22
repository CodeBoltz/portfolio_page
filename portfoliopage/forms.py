from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=120), ])
    content = StringField('Content',validators=[DataRequired(), Length(min=2, max=1200), ])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember = BooleanField('Remember Me')
   submit = SubmitField('Login')

class DesignForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200), ])
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200), ])
    