from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import PasswordField, StringField, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, BooleanField,FileField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
#from flask.ext.uploads import UploadSet, IMAGES
#images = UploadSet('images', IMAGES)
#DB
from . models import Subscriber

###########################################################################
###########################################################################
###########################################################################
### customized classes (functions)
###########################################################################
###########################################################################
###########################################################################
class ReadonlyStringField(StringField):
  def __call__(self, *args, **kwargs):
    kwargs.setdefault('readonly', True)
    return super(ReadonlyStringField, self).__call__(*args, **kwargs)
class ReadonlyCheckboxField(BooleanField):
  def __call__(self, *args, **kwargs):
    kwargs.setdefault('readonly', True)
    kwargs.setdefault('disabled', 'disabled')
    return super(ReadonlyCheckboxField, self).__call__(*args, **kwargs)
###########################################################################

###########################################################################
###########################################################################
###########################################################################
### Define the forms (WTForms)
###########################################################################
###########################################################################
###########################################################################
class ContactUsForm(FlaskForm):
    """
    Form for users to contact us
    """
    firstName = StringField('First Name', validators=[DataRequired('please enter your first name')])
    lastName = StringField('Last Name', validators=[DataRequired()])
    company = StringField('Your Organization')
    jobTitle = StringField('Job Title')
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact_message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Contact Us')
   #Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   #email = TextField("Email",[validators.Required("Please enter your email address."),
   #validators.Email("Please enter your email address.")])
   #Age = IntegerField("age")
   #language = SelectField('Languages', choices = [('cpp', 'C++'),
   #   ('py', 'Python')])
###########################################################################
###########################################################################
###########################################################################
class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    form_action = StringField('Action',default='register')
    form_action.default = 'register'

    email = StringField('Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    #userName = StringField('userName', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired('please enter Your first name')])
    lastName = StringField('Last Name', validators=[DataRequired('please enter Your last name')])
    agreeTerms = BooleanField('agree terms', validators=[DataRequired('please agree with our terms and conditions')])
    mailingListSignUp = BooleanField('mailing list signup')
    company = StringField('Your Organization')
    jobTitle = StringField('Job Title')
    rememberMe = BooleanField('Remember Me')
    password = PasswordField('Password', validators=[
                                        DataRequired('please enter Your password'),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired('please confirm Your password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def validate_xemail(self, field):
        if Subscriber.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_agreeTerms(self, field):
        if not(field.data):
            raise ValidationError('You must agree with our terms and conditions')

    def validate_xuserName(self, field):
        if Subscriber.query.filter_by(userName=field.data).first():
            raise ValidationError('userName is already in use.')
###########################################################################
###########################################################################
###########################################################################
class UserProfileDisplayForm(FlaskForm):
    """
    Form for User Profile
    """
    email = ReadonlyStringField('Email')
    userName = ReadonlyStringField('userName')
    firstName = ReadonlyStringField('First Name')
    lastName = ReadonlyStringField('Last Name')
    company = ReadonlyStringField('Company')
    jobTitle = ReadonlyStringField('jobTitle')
    mobile = ReadonlyStringField('mobile')

    mailingListSignUp = ReadonlyStringField('mailing list signup')
    termsAgreed = ReadonlyStringField('Terms Agreed')
    registered = ReadonlyStringField('Registered')
    lastLogin = ReadonlyStringField('Last Login')
    mobileConfirmed = ReadonlyStringField('mobile confirmed')
    emailConfirmed = ReadonlyStringField('email confirmed')

    #passwordHash = db.Column(db.String(128))
    #departmentID = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #roleID = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #isAdmin = db.Column(db.Boolean, default=False)
    #confirmed = db.Column(db.Boolean, nullable=False, default=False)
    #confirmedDT = db.Column(db.DateTime, nullable=True)
    #mobileConfirmed = db.Column(db.Boolean, nullable=False, default=False)
    #emailConfirmed = db.Column(db.Boolean, nullable=False, default=False)
###########################################################################
###########################################################################
###########################################################################
class UserProfileChangeForm(FlaskForm):
    """
    Form for User Profile Change
    """
    email = StringField('Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    userName = StringField('userName')
    firstName = StringField('First Name', validators=[DataRequired('please enter Your first name')])
    lastName = StringField('Last Name', validators=[DataRequired('please enter Your last name')])
    company = StringField('Your Organization')
    jobTitle = StringField('Job Title')
    mobile = StringField('Mobile', )
    mailingListSignUp = BooleanField('mailing list signup')

    submit = SubmitField('Update')

    def validate_xemail(self, field):
        if Subscriber.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_xuserName(self, field):
        if Subscriber.query.filter_by(userName=field.data).first():
            raise ValidationError('userName is already in use.')
###########################################################################
###########################################################################
###########################################################################
class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired('please enter Your password')])
    rememberMe = BooleanField('Remember Me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

    def validate_email(self, field):
        if not(Subscriber.query.filter_by(email=field.data).first()):
            raise ValidationError('invalid email or password')

    def validate_xpassword(self,field):
        employee = Subscriber.query.filter_by(email=self.email.data).first()
        #when login details are correct
        if employee is None:
            raise ValidationError('invalid email or password')
        else:
            if not(Subscriber.verify_password(field)):
                raise ValidationError('invalid email or password')
###########################################################################
###########################################################################
###########################################################################
class PasswordChangeForm(FlaskForm):
    """
    Form for subscribers to change their password
    """
    email = StringField('Email') # we need it for forget password...
    old_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm New Password',validators=[DataRequired(),EqualTo('new_password')])
    submit = SubmitField('Update')
###########################################################################
###########################################################################
###########################################################################
class mobileConfirmationForm(FlaskForm):
    """
    Form for subscribers to confirm their mobile
    """
    mobile = ReadonlyStringField('mobile')
    mobile_token = StringField('confirmation code', validators=[DataRequired()])
    submit = SubmitField('Confirm')
###########################################################################
###########################################################################
###########################################################################
class emailConfirmationForm(FlaskForm):
    """
    Form for subscribers to confirm their email
    """
    email = ReadonlyStringField('email')
    submit = SubmitField('send new confirmation Email')
###########################################################################
###########################################################################
###########################################################################
class forgetPasswordForm(FlaskForm):
    """
    Form for subscribers to request a confirmation email when they forget their password
    """
    email = StringField('Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    recaptcha = RecaptchaField()
    submit = SubmitField('send confirmation Email')
###########################################################################
###########################################################################
###########################################################################
class PasswordReSetForm(FlaskForm):
    """
    Form for subscribers to reset their password when they forget their password(without login and after confirming their email)
    """
    email = ReadonlyStringField('email')
    new_password = PasswordField('New Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm New Password',validators=[DataRequired(),EqualTo('new_password')])
    submit = SubmitField('Update')
###########################################################################
###########################################################################
###########################################################################
class EmailChangeForm(FlaskForm):
    """
    Form for subscribers to change their email
    """
    old_email = StringField('Current Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    new_email = StringField('New Email', validators=[DataRequired('please enter Your New email address'), Email('please enter a valid email address'),EqualTo('confirm_email')])
    confirm_email = StringField('Confirm New Email', validators=[DataRequired('please enter Your New email address'), Email('please enter a valid email address')])
    submit = SubmitField('Update')
###########################################################################
###########################################################################
###########################################################################
class SubscriberForm(FlaskForm):
    """
    Form for subscribers to maintain their profile
    """
    email = StringField('Email', validators=[DataRequired('please enter Your email address'), Email('please enter a valid email address')])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    mobile = StringField('mobile', validators=[DataRequired()])
    #mobile_token = StringField('mobile token', validators=[DataRequired()])

    submit = SubmitField('Update')

    #def validate_email(self, field):
    #    if Subscriber.query.filter_by(email=field.data).first():
    #        raise ValidationError('Email is already in use.')

    #def validate_userName(self, field):
    #    if Subscriber.query.filter_by(userName=field.data).first():
    #        raise ValidationError('userName is already in use.')
###########################################################################
###########################################################################
###########################################################################
class AvatarUploadForm(FlaskForm):
    """
    Form for subscribers to upload their Avatar picture
    """
    #photo = FileField('Your Avatar',validators=[FileRequired('no file!'),FileAllowed(['jpg', 'png'], 'Images only!')])
    photo = FileField('Your Avatar',validators=[FileRequired('no file!'),FileAllowed('Images only!')])
    emptyAvatarType = RadioField('avatar', choices = [('F','Female'), ('M','Male')])
    submit = SubmitField('Upload')
    def validate_sphoto(self, field):
        if not(field.data) and emptyAvatarType not in (['F','M']):
            raise ValidationError('select an image file or an empty avatar')
###########################################################################
###########################################################################
###########################################################################

