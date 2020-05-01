from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

class DesignForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    date = StringField('Date', validators=[DataRequired(), Length(min=2, max=200)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=1200)])
    image = FileField('First Image', validators=[DataRequired()])
    image2 = FileField('Second Image', validators=[])
    image3 = FileField('Third Image', validators=[])
    link = StringField('Social Link', validators=[DataRequired(), Length(min=2, max=2000)])
    submit = SubmitField('Upload')
    