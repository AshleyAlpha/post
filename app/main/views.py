from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PostForm,CommentsForm,SubForm,UpdatePostForm
from ..models import User,Post,Comment,Subscribe
from flask_login import login_required,current_user
from .. import db
from ..request import get_quote
from ..email import mail_message


@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    quote=get_quote()
    # print(quote)
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
    subscribers=Subscribe.query.all()
    if form.validate_on_submit():
        content=form.content.data
        new_post=Post(content = content,user=current_user)

        db.session.add(new_post)
        db.session.commit()
        for subscriber in subscribers:
          mail_message("hello! there is new post","email/notification",subscriber.email)


        return redirect(url_for('main.index'))

    return render_template('post.html',form = form) 

@main.route('/edit/post/<int:id>',methods= ['GET','POST'])
@login_required
def update_post(id):
   post=Post.query.filter_by(id=id).first()
   if post is None:
        abort(404)

   form=UpdatePostForm()
   if form.validate_on_submit():
        #  post.title=form.title.data
         post.content=form.content.data

         db.session.add(post)
         db.session.commit()

         return redirect(url_for('main.index'))
   return render_template('update_post.html',form=form)

@main.route('/delete/post/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_post(id):
    post=Post.query.filter_by(id=id).first()
    title = 'Home'
    
    if post is not None:
       post.delete_post()
       return redirect(url_for('main.index'))
    return render_template('index.html', title = title, post=post,quote=quote)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def comments(id):
    form = CommentsForm()
    if form.validate_on_submit():
        names=form.names.data
        comment=form.comment.data
        new_comment=Comment(comment=comment,names=names ,posts_id = id,user=current_user)
        

        db.session.add(new_comment)
        db.session.commit()
    comment=Comment.query.filter_by(posts_id=id).all()

    return render_template('comment.html',comment=comment,form = form)

@main.route('/delete/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    form = CommentsForm()
    comment=Comment.query.filter_by(id=id).first()
 

    if comment is not None:
       comment.delete_comment()
       return redirect(url_for('main.index'))

    return render_template('comment.html',form = form)

@main.route('/subscriber/new/', methods=['GET','POST'])
def subscribe():
    form=SubForm()
    if form.validate_on_submit():
        email=form.email.data
        new_subscriber=Subscribe(email=email)

        db.session.add(new_subscriber)
        db.session.commit()
        mail_message("Thank you for subscribing","email/subscribing",new_subscriber.email)
        
        return redirect(url_for('main.index'))

    return render_template('subscriber.html',form = form)
