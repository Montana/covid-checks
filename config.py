import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  
    ENV = os.environ.get('FLASK_ENV')
    ORG = os.environ.get('ORG')
    APP_BASE_URL = os.environ.get('APP_BASE_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'who wants to know'
    TIMEZONE = os.environ.get('TIMEZONE')
    BOOTSTRAP_EMAIL = os.environ.get('BOOTSTRAP_EMAIL')
    BOOTSTRAP_PASS = os.environ.get('BOOTSTRAP_PASS')
    BOOTSTRAP_USERNAME = os.environ.get('BOOTSTRAP_USERNAME')
    SECURITY_POST_LOGIN_VIEW = '/home'
    SECURITY_CHANGEABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = True
    ID_SALT=os.environ.get('ID_SALT')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    BOOTSTRAP_SERVE_LOCAL = True
    SECURITY_USER_IDENTITY_ATTRIBUTES=['email', 'username']
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER')
    EMAIL_PLAINTEXT = True
    EMAIL_HTML = False
    TEMP_UNITS_ENCODING = os.environ.get('TEMP_UNITS_ENCODING') or '&#8457;'
    POSTS_PER_PAGE = 1
