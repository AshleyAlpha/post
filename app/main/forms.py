from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class PostForm(FlaskForm):
     content = TextAreaField('write Your Post', validators=[Required()])
     submit = SubmitField('Submit!')

class CommentsForm(FlaskForm):
    names = TextAreaField('names', validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('SUBMIT')  

class SubForm(FlaskForm):
    email = TextAreaField('input your email', validators=[Required()])
    submit = SubmitField('SUBMIT')  
class UpdatePostForm(FlaskForm):
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')


