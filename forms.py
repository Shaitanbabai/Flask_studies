from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, FileField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    birth_date = DateField('Дата рождения', format='%Y-%m-%d', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    photo = FileField('Фото', validators=[DataRequired()])
    submit = SubmitField('Отправить')