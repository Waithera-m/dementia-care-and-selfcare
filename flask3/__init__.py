from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__) 
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'c26d6bde3e77e96c634e8a88fd857560'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://mary:pixie01@localhost/dementia'
db = SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flask3 import routes