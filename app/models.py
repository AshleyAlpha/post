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
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches=db.relationship('Pitch',backref='user',lazy='dynamic')
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

class Pitch(db.Model):
    __tablename__= 'pitches' 
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    category = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship('Comment',backref='pitch',lazy='dynamic')
    def __repr__(self):
        return f'User {self.content}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __repr__(self):
        return f'User {self.comment}'
def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()
