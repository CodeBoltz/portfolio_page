from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from models import Admin

class DesignForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    date = StringField('Date', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1200)])
    image = FileField('First Image', validators=[DataRequired()])
    image2 = FileField('Second Image', validators=[])
    image3 = FileField('Third Image', validators=[])
    link = StringField('Social Link', validators=[DataRequired(), Length(min=2, max=2000)])
    submit = SubmitField('Upload')
    
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()] )
    subject  = StringField('Subject', validators=[DataRequired(), Length(min=2, max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=2, max=2000)])
    submit = SubmitField('Send email')