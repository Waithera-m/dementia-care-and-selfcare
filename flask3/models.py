
from datetime import datetime
from flask3 import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment',backref='post',lazy='dynamic')


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
    def __repr__(self):
        return f"Comment('{self.content}', '{self.date_posted}')"
class DementiaNews():

    '''
    class facilitates the creation of news articls objects
    '''
    def __init__(self,author,title,publishedAt,description,url,urlToImage):

        '''
        Method facilitates the definition of objects; properties

        Args:
            author (str): article's author 
            title (str): article's title
            publishedAt (str): article publication date
            description (str): brief description of article content
            url (str): link to full article
        '''

        
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        self.urlToImage = urlToImage