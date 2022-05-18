from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class Intform(FlaskForm):
    id = IntegerField('GameID', validators=[DataRequired()],)
    