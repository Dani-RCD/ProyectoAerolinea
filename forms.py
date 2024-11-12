from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class VueloForm(FlaskForm):
    vuelo_id = StringField('ID del Vuelo', validators=[DataRequired()])
    matricula = StringField('Matrícula', validators=[DataRequired()])
    submit = SubmitField('Crear Vuelo')

class ReservaForm(FlaskForm):
    # Define campos para reservar el vuelo si se requiere
    pass

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')])
    submit = SubmitField('Registrar')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password', message="Las contraseñas deben coincidir")])
    role = SelectField('Rol', choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')], validators=[DataRequired()])
    submit = SubmitField('Registrarse')
