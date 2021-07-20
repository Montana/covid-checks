from app import app
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length, Regexp, Optional, NumberRange
from wtforms.fields.html5 import TelField, DateField, DecimalField
from app.models import Users, Role
import re


def get_roles():
    try:
        roles = Role.query.all()
        choose = 'Choose...'
        container = [('', choose)]
        for role in roles:
            container.append((role.name, role.name))
        return container
    except Exception as e:
        return [('error', 'error')]


def decimal_validation(form, field):
    pattern = re.compile('^\d{2,3}(\.\d{1})?$')
    if not pattern.fullmatch(str(field.data)):
        raise ValidationError(
            '0 to 1 decimal variable')


class ReadingsForm(FlaskForm):
    temp = DecimalField('Temperature',
                        validators=[
                            DataRequired(message='This field is required'),
                            decimal_validation
                        ])
    oximeter = DecimalField('Oximeter',
                            validators=[
                                DataRequired(message='This field is required'),
                                decimal_validation
                            ])
    symptoms = BooleanField('Have you or currently been experiencing COVID-19 symptoms?',
                            validators=[])
    working_btn = SubmitField("I'm working the shift")
    not_working_btn = SubmitField("I'm going home to sleep.")


class AddUser(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(message='This field is required.'),
                            Email(message='A valid email address is required.')
                        ])
    username = StringField(
        'Username',
        validators=[DataRequired(message='This field is required')])
    roles = SelectField('Role', choices=get_roles())
    submit = SubmitField("Add")
