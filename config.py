import os

class Config:

    '''
    class facilitates the creation of app configurations
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    print(NEWS_API_KEY)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SECRET_KEY)
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    print(MAIL_USERNAME)
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    

class DevConfig(Config):

    '''
    class inherits general configurations from Config class
    '''

    DEBUG = True

class TestConfig(Config):

    '''
    class inherits general configurations from config class
    '''
    pass

class ProdConfig(Config):

    '''
    class inherits general configurations from config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}