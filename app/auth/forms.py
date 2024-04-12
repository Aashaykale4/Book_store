from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,PasswordField,BooleanField

from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

from app.auth.models import User

#can be done for user too
def email_exists(form,field):
    email=User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError("Email Already exists")
    
def user_exists(form,field):
    user=User.query.filter_by(user_email=field.data).first()
    if user:
        raise ValidationError("Name Already exists")

class RegistrationForm(FlaskForm):
    name=StringField(" Name",validators=[DataRequired(),Length(3,10,message=' between 3-10 char'),user_exists])
    email=StringField(" Email",validators=[DataRequired(),Email(),email_exists])
    password=PasswordField('password',validators=[DataRequired(),Length(6),EqualTo('confirm')])
    confirm=PasswordField('Confirm',validators=[DataRequired()])
    submit=SubmitField("Register")


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    stayloggedin=BooleanField('stay logged-in')
    submit=SubmitField('LogIn')