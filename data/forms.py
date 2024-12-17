from flask_wtf import FlaskForm
import wtforms


class SingUpForm(FlaskForm):
    username = wtforms.StringField("Введіть логін", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Введіть електронну пошту",validators=[wtforms.validators.DataRequired(),wtforms.validators.Email()])
    password = wtforms.PasswordField("Пароль",validators=[wtforms.validators.DataRequired(),wtforms.validators.length(8)])
    sumbit = wtforms.SubmitField("Зареєструватись")


class LoginForm(FlaskForm):
    username = wtforms.StringField("Введіть логін aбо електронну пошту", validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Пароль",validators=[wtforms.validators.DataRequired()])
    sumbit = wtforms.SubmitField("Зареєструватись")
