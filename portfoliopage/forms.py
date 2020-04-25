from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

class DesignForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200), ])
    date = StringField('Date', validators=[DataRequired(), Length(min=2, max=200), ])
    image = FileField('Image', validators=[FileRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=1200), ])
    
    