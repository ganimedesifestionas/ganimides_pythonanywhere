# myApp/module_authorization/models.py
from flask_login import UserMixin
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)

# Import the database object (db) from the main application module. We define the db inside /myApp/__init__.py
from ..import db
from ..import login_manager

# Define a reusable base model for other database tables to inherit (will be part of all defined tables)
class Base(db.Model):
    __abstract__  = True
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    id            = db.Column(db.Integer, primary_key=True)

###########################################################################
class VisitPoint(Base):
    """
    Create a Visitors table in mySQL
    """
    # Ensures table will be named in plural and not in singular, as is the name of the model
    __tablename__ = 'visitpoints'

    id = db.Column(db.Integer, primary_key=True)
    visitpointNumber = db.Column(db.Integer, nullable=True, default=1)
    geolocation_type = db.Column(db.String(20),default='')
    ip = db.Column(db.String(60), index=True)
    latitude = db.Column(db.Numeric(15,9), index=True)
    longitude = db.Column(db.Numeric(15,9), index=True)
    visitDT = db.Column(db.DateTime, nullable=False)
    firstvisitDT = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    lastvisitDT = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    visitsCount = db.Column(db.Integer, nullable=True, default=1)
    visits = db.relationship('Visit', backref='visitpoint')

    iptype = db.Column(db.String(60), nullable=True, default='')
    continent_code = db.Column(db.String(10), nullable=True, default='')
    continent_name = db.Column(db.String(60), nullable=True, default='')
    country_code = db.Column(db.String(10), nullable=True, default='')
    country_name = db.Column(db.String(60), nullable=True, default='')
    region_code = db.Column(db.String(10), nullable=True, default='')
    region_name = db.Column(db.String(60), nullable=True, default='')
    city = db.Column(db.String(60), nullable=True, default='')
    zip = db.Column(db.String(60), nullable=True, default='')
    postal_code = db.Column(db.String(60), nullable=True, default='')
    address = db.Column(db.String(255), nullable=True, default='')
    location = db.Column(db.PickleType, nullable=True, default=None) # this is a blob datatype to add dictionary, json etc

    #timezone = db.Column(db.String(60), nullable=True, default='')
    #currency = db.Column(db.String(10), nullable=True, default='')
    #connection = db.Column(db.String(60), nullable=True, default='')
    #security = db.Column(db.String(60), nullable=True, default='')

    # Just set the attribute to save it
    #s = SomeEntity(attributes={'baked': 'beans', 'spam': 'ham'})
    #session.add(s)
    #session.commit()

    # If mutable=True on PickleType (the default) SQLAlchemy automatically
    # notices modifications.
    #s.attributes['parrot'] = 'dead'
    #session.commit()
    # var apistack geolocation result={'ip': '213.149.173.194', 'type': 'ipv4', 'continent_code': 'EU', 
    # 'continent_name': 'Europe', 
    # 'country_code': 'CY', 'country_name': 'Cyprus', 'region_code': '02', 
    # 'region_name': 'Limassol', 'city': 'Limassol', 'zip': None, 'latitude': 34.6841, 'longitude': 33.0379, 
    # 'location': {'geoname_id': 146384, 'capital': 'Nicosia', 
    # 'languages': [{'code': 'el', 'name': 'Greek', 'native': 'Ελληνικά'}, 
    # {'code': 'tr', 'name': 'Turkish', 'native': 'Türkçe'}, 
    # {'code': 'hy', 'name': 'Armenian', 'native': 'Հայերեն'}], 
    # 'country_flag': 'http://assets.ipstack.com/flags/cy.svg', 
    # 'country_flag_emoji': '🇨🇾', 'country_flag_emoji_unicode': 'U+1F1E8 U+1F1FE', 
    # 'calling_code': '357', 
    # 'is_eu': True}}
    # 2019-02-09 07:40:47     var ---ip=213.149.173.194
    # 2019-02-09 07:40:47     var ---type=ipv4
    # 2019-02-09 07:40:47     var ---continent_code=EU
    # 2019-02-09 07:40:47     var ---continent_name=Europe
    # 2019-02-09 07:40:47     var ---country_code=CY
    # 2019-02-09 07:40:47     var ---country_name=Cyprus
    # 2019-02-09 07:40:47     var ---region_code=02
    # 2019-02-09 07:40:47     var ---region_name=Limassol
    # 2019-02-09 07:40:47     var ---city=Limassol
    # 2019-02-09 07:40:47     var ---zip=None
    # 2019-02-09 07:40:47     var ---latitude=34.6841
    # 2019-02-09 07:40:47     var ---longitude=33.0379
    # 2019-02-09 07:40:47     var ---location={'geoname_id': 146384, 'capital': 'Nicosia', 'languages': [{'code': 'el', 'name': 'Greek', 'native': 'Ελληνικά'}, {'code': 'tr', 'name': 'Turkish', 'native': 'Türkçe'}, {'code': 'hy', 'name': 'Armenian', 'native': 'Հայերեն'}], 'country_flag': 'http://assets.ipstack.com/flags/cy.svg', 'country_flag_emoji': '🇨🇾', 'country_flag_emoji_unicode': 'U+1F1E8 U+1F1FE', 'calling_code': '357', 'is_eu': True}

    #email = db.Column(db.String(120), index=True, unique=True)
    #userName = db.Column(db.String(60), index=True, unique=True , default='')
    #firstName = db.Column(db.String(60), index=True , default='')
    #lastName = db.Column(db.String(60), index=True , default='')
    #roleX = db.Column(db.String(60), index=True , default='')
    #mobile = db.Column(db.String(20), index=True , default='')
    #company = db.Column(db.String(60), index=True , default='')
    #jobTitle = db.Column(db.String(60), index=True , default='')
    #agreeTerms = db.Column(db.Boolean, nullable=False, default=False)
    #agreeTermsDT = db.Column(db.DateTime, nullable=True)
    #mailingListSignUp = db.Column(db.Boolean, nullable=False, default=False)
    #mailingListSignUpDT = db.Column(db.DateTime, nullable=True)
    #rememberMe = db.Column(db.Boolean, nullable=False, default=False)
    #passwordHash = db.Column(db.String(128) , default='')
    #passwordReset = db.Column(db.Boolean, nullable=False, default=False)
    #confirmedDT = db.Column(db.DateTime, nullable=True)
    #lastLoginDT = db.Column(db.DateTime, nullable=True)
    #mobileConfirmed = db.Column(db.Boolean, nullable=False, default=False)
    #mobileConfirmedDT = db.Column(db.DateTime, nullable=True)
    #emailConfirmed = db.Column(db.Boolean, nullable=False, default=False)
    #emailConfirmedDT = db.Column(db.DateTime, nullable=True)
    #mobileConfirmationCodeHash = db.Column(db.String(128), nullable=True,default='')
    #mobileConfirmationCodeDT = db.Column(db.DateTime, nullable=True)
    #avatarImageFile = db.Column(db.String(255), nullable=True)
    #accessModules = db.Column(db.String(255), nullable=True)
    #departmentID = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #roleID = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #isAdmin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<visitpoint: {0}({1}) {5}/{6} ip:{2} lat:{3} lon:{4}>'.format(self.id, self.visitpointNumber, self.ip, self.latitude,self.longitude,self.country_name,self.city)
###########################################################################
class Visit(Base):
    """
    Create a Visits table in mySQL
    """
    # Ensures table will be named in plural and not in singular, as is the name of the model
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    visitNumber = db.Column(db.Integer, nullable=True, default=0)
    visitDT = db.Column(db.DateTime, nullable=False)
    sessionID = db.Column(db.String(255), nullable=True, default='')
    #ip = db.Column(db.String(60), index=True)
    #latitude = db.Column(db.Numeric(15,12), index=True)
    #longitude = db.Column(db.Numeric(15,12), index=True)
    visitpoint_ID = db.Column(db.Integer, db.ForeignKey('visitpoints.id'))
    pagesVisitedCount = db.Column(db.Integer, nullable=True, default=0)
    def __repr__(self):
        return '<visit: {0}({1}) {2} visitpoint:{3}>'.format(self.id, self.visitNumber, self.visitDT, self.visitpoint_ID)
    def __str__(self):
        return '{0}'.format(self.visitDT)

class Page_Visit(Base):
    """
    Create a page Visits table in mySQL
    """
    __tablename__ = 'page_visits'

    id = db.Column(db.Integer, primary_key=True)
    #clientIPA = db.Column(db.String(60), nullable=True, default='')
    pageID = db.Column(db.String(60), nullable=True, default='')
    pageType = db.Column(db.String(60), nullable=True, default='')
    pageLanguage = db.Column(db.String(60), nullable=True, default='')
    pageFunction = db.Column(db.String(60), nullable=True, default='')
    pageURL = db.Column(db.String(1024), nullable=True, default='')
    request_method = db.Column(db.String(60), nullable=True, default='')
    pageTemplate = db.Column(db.String(1024), nullable=True, default='')
    pageTemplate_page = db.Column(db.String(1024), nullable=True, default='')
    pageTemplate_form = db.Column(db.String(1024), nullable=True, default='')
    sessionID=db.Column(db.String(255), nullable=True, default='')
    #ip = db.Column(db.String(60), index=True)
    #latitude = db.Column(db.Numeric(15,12), index=True)
    #longitude = db.Column(db.Numeric(15,12), index=True)
    #visitpoint_ID = db.Column(db.Integer, db.ForeignKey('visitpoints.id'))
    visit_ID = db.Column(db.Integer, db.ForeignKey('visits.id'))

    def __repr__(self):
        return '<page_visit:{0} page:{1}>'.format(self.id, self.pageID)

class xContactMessage(db.Model):
    """
    Create a ContactMessage table
    """

    # Ensures table will be named in plural and not in singular, as is the name of the model
    __tablename__ = 'xcontactmessages'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    jobTitle = db.Column(db.String(60), index=True , default='')
    company = db.Column(db.String(60), index=True)
    message = db.Column(db.String(1024))
    mobile = db.Column(db.String(20), index=True)
    receivedDT = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmedDT = db.Column(db.DateTime, nullable=True)
    repliedDT = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<ContactMessage: {}>'.format(self.message)

    def json_view(self):

        if self.confirmed:
            confirmatonString=str(self.confirmedDT)
        else:
            confirmatonString=''

        if self.repliedDT:
            repliedString=str(self.repliedDT)
        else:
            repliedString=''

        receivedString=str(self.receivedDT)

        rec = {
            'id':self.id
            ,'firstName':self.firstName
            ,'lastName':self.lastName
            ,'email':self.email
            ,'company':self.company
            ,'title':self.jobTitle
            ,'mobile':self.mobile
            ,'receivedDT':receivedString
            ,'confirmed':confirmatonString
            ,'repliedDT':repliedString
        }

        return rec

# Set up user_loader
#@login_manager.user_loader
#def load_user(user_id):
#    return Subscriber.query.get(int(user_id))