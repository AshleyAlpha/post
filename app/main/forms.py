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
class PitchForm(FlaskForm):
     content = TextAreaField('write Your Pitch', validators=[Required()])
     submit = SubmitField('Submit!')

# class CommentsForm(FlaskForm):
#     comment = TextAreaField('Comment', validators=[Required()])
#     # vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
#     submit = SubmitField('SUBMIT')  

# class AddPitch(FlaskForm):
#     category=SelectField('category:'choices=[('pickup-lines','pickup-lines'),('interview-pitches','interview-pitches'),('promotion-pitches','promotion-pitches')])
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')