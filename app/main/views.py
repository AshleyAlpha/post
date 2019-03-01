from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PostForm,CommentsForm
from ..models import User,Post,Comment
from flask_login import login_required,current_user
from .. import db

@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    quote=get_quote()
    post=Post.query.all()
    return render_template('index.html', title = title, post=post,quote=quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/post/new', methods=['GET','POST'])
@login_required
def create_posts():
    form = PostForm()
    if form.validate_on_submit():
        content=form.content.data
        new_post=Post(content = content,user=current_user)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('post.html',form = form)  

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
# @login_required
def comments(id):
    form = CommentsForm()
    if form.validate_on_submit():
        comment=form.comment.data
        new_comment=Comment(comment=comment,posts_id = id,user=current_user)

        db.session.add(new_comment)
        db.session.commit()

    comment=Comment.query.filter_by(posts_id=id).all()

    return render_template('comment.html',comment=comment,form = form)