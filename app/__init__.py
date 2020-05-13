from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_simplemde import SimpleMDE

simplemde = SimpleMDE()


csrf = CSRFProtect()

mail=Mail()

db=SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):

    '''
    function facilitates app and extension initialization, blueprint registration, and app configurations creation
    '''

    #create flask instance
    app = Flask(__name__)

    #configurations creation
    app.config.from_object(config_options[config_name])

   
    #extensions initialization
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    

    #blueprint registration
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app