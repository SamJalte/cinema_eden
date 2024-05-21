from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class RegistrationForm(FlaskForm):
    fname = StringField(
        "Prénom", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Nom", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Nom d'utilisateur", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirmer mot de passe", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("S'inscrire")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Se souvenir de moi")
    submit = SubmitField("Se connecter")