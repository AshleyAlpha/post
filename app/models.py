from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posts=db.relationship('Post',backref='user',lazy='dynamic')
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__= 'posts' 
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship('Comment',backref='post',lazy='dynamic')
    def __repr__(self):
        return f'User {self.content}'

    def delete_post(self):
       db.session.delete(self)
       db.session.commit()

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    names = db.Column(db.String(255), index=True)
    comment = db.Column(db.String(255))
    posts_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __repr__(self):
        return f'User {self.comment}'
    
    def delete_comment(self):
       db.session.delete(self)
       db.session.commit()

class Subscribe(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    def __repr__(self):
        return f'User {self.email}'

class Quote:

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self. quote = quote

