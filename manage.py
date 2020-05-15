from flask3 import app,db
from flask3.models import User
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand




manager = Manager(app)

manager.add_command('server',Server)

migrate =Migrate (app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def create_shell():

    return dict(app=app,db=db,User=User)


if __name__ == '__main__':
    manager.run()