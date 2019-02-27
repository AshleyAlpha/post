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
# class AddPitch(FlaskForm):
#     category=SelectField('category:'choices=[('pickup-lines','pickup-lines'),('interview-pitches','interview-pitches'),('promotion-pitches','promotion-pitches')])
#     bio = TextAreaField('pitch.',validators = [Required()])
#     submit = SubmitField('SUBMIT')