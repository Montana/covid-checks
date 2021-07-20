from app import app
from app import db
from config import Config
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from sqlalchemy import ForeignKey, desc, text
from sqlalchemy.orm import relationship
import uuid
import re
from datetime import datetime, timedelta, date
import random
import string
from app.utilities import Utilities

roles_users = db.Table(
    'roles_users', db.Column('user_id', db.String(),
                             db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    description = db.Column(db.String())


class Users(db.Model, UserMixin):
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid1()))
    email = db.Column(db.String(), unique=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    created = db.Column(db.DateTime, index=True)
    username = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    status = db.Column(db.String)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role',
                            secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    readings = db.relationship('Readings',
                               backref=db.backref('users'),
                               order_by=desc(text('Readings.created')))

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)
        self.id = str(uuid.uuid1())
        self.created = datetime.utcnow()

    def reading_today(self):
        
        if len(self.readings) < 1:
            return False
        else:
            if Utilities.get_date() == self.readings[0].reading_date:
                return True
            else:
                return False

    def random_password():
      
        hex_value = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
            'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'
        ]
        base = str(uuid.uuid4())
        pass_arr = []
        for _ in range(12):
            pass_arr.append(hex_value[random.randint(0, len(hex_value) - 1)])
        return '{}-{}'.format(''.join(pass_arr), base[0:7])

    def normalize_phone(self, input, region='US'):
      
        if region == 'US':
            fancy_num = re.search(
                r'^\((?P<area>\d{3})\)\s?(?P<prefix>\d{3})-(?P<subscriber>\d{4})$',
                input,
                flags=re.IGNORECASE)
            if fancy_num:
                normalized = '+1' + str(fancy_num.group('area')) + str(
                    fancy_num.group('prefix')) + str(
                        fancy_num.group('subscriber'))
                return normalized
            straight_num = re.search(r'^(?P<number>\d{10})$',
                                     input,
                                     flags=re.IGNORECASE)
            if straight_num:
                normalized = '+1' + straight_num.group('number')
                return normalized


class Readings(db.Model):
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid1()))
    created = db.Column(db.DateTime, index=True)
    reading_date = db.Column(db.String)
    temp = db.Column(db.String)
    oximeter = db.Column(db.String)
    status = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    symptoms = db.Column(
        db.Boolean
    )  # True == user indicated "symptoms" and system default is Reading == not-working

    def __init__(self, **kwargs):
        super(Readings, self).__init__(**kwargs)
        self.id = str(uuid.uuid1())
        self.created = datetime.utcnow()
        self.reading_date = Utilities.get_date()
        if self.status == True:
            self.status = 'working'
        else:
            self.status = 
        if self.symptoms == 'yes':
            self.symptoms = True
            self.status = 'not going to complete shift'

    def get_username(self):
      
    queryset = UserModel.objects.all()

    user_id = self.request.query_params.get('user_id', None)

    # If user_id param is not None, filter using the obtained user_id
    
    if user_id is not None:
        queryset = queryset.filter(id=user_id)

    return queryset
