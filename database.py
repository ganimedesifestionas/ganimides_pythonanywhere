# application database init
"""
This script creates default database entries
"""
import os
import sqlalchemy
#from sqlalchemy.engine.url import URL
#import pymysql
#pymysql.install_as_MySQLdb()
#import MySQLdb
#from sqlalchemy import create_engine
#from flask_sqlalchemy import SQLAlchemy
from website_app import db
from website_app import app as application
from website_app.module_administration.models import User, Department, Role
from website_app.module_authorization.models import Subscriber, ContactMessage
from website_app.models import Visit, VisitPoint, Page_Visit, xContactMessage
from website_app.debug_services.debug_log_services import *
app = application
app.app_context().push()

#log_start('application_databases')

DATABASE_SERVER = app.config['DATABASE_SERVER']
DATABASE_SERVER_URI = app.config['DATABASE_SERVER_URI']
DATABASE_NAME = app.config['DATABASE_NAME']
DATABASE_URI = app.config['DATABASE_URI']

#log_variable('DATABASE_SERVER_URI', DATABASE_SERVER_URI)
#log_variable('DATABASE_URI', DATABASE_URI)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create_database():
    log_start('create_database')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI

    dbserver_engine = sqlalchemy.create_engine(DATABASE_SERVER_URI, pool_recycle=180) # connect to server
    existing_databases = dbserver_engine.execute("SHOW DATABASES;")
    existing_databases = [d[0] for d in existing_databases]
    # for database in existing_databases:
    #     print("...database {0} on dbserver {1}".format(database, DATABASE_SERVER_URI))
    if DATABASE_NAME not in existing_databases:
        dbserver_engine.execute("CREATE DATABASE {db}".format(db=DATABASE_NAME))
        log_warning("{0} database CREATED on DBserver {1}".format(DATABASE_NAME, DATABASE_SERVER))
    else:
        log_info("database {0} already exists on DBserver {1}".format(DATABASE_NAME, DATABASE_SERVER))
    # -or-
    # dbserver_engine.execute("CREATE DATABASE IF NOT EXISTS {db}".format(db=DATABASE_NAME))
    # dbserver_engine.execute("USE {db}".format(db=DATABASE_NAME))
    dbserver_engine.dispose()
    log_finish('create_database')

def create_all_tables_auto():
    log_start('create_all_tables_auto')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    #log_info('database-init',  'create all tables in database if not exists(auto)')
    #log_info('database-init',  '   DATABASE_URI =',DATABASE_URI)
    db_engine = sqlalchemy.create_engine(DATABASE_URI, pool_recycle=180) # connect to database
    existing_tables_before = get_tables_list(db_engine)
    #log_info('database-init',  'tables before')
    #list_tables(db_engine)
    db.create_all(app=app)
    db.session.commit()
    existing_tables_after = get_tables_list(db_engine)
    created = 0
    for table in existing_tables_after:
        if table not in existing_tables_before:
            created = created + 1
    log_warning("{0} tables created in database {1}".format(created,DATABASE_NAME))
    #db_engine.dispose()
    log_finish('create_all_tables_auto')

def create_all_tables_manually():
    log_start('create_all_tables_manually')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    #log_info('database-init',  'create tables in database if not exists (manually)')
    #log_info('database-init',  '   DATABASE_URI =', DATABASE_URI)
    db_engine = sqlalchemy.create_engine(DATABASE_URI, pool_recycle=180) # connect to database
    existing_tables_before = get_tables_list(db_engine)

    thistable=Visit.__table__.name
    if thistable.lower() not in existing_tables:
        Department.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=VisitPoint.__table__.name
    if thistable.lower() not in existing_tables:
        Department.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=Page_Visit.__table__.name
    if thistable.lower() not in existing_tables:
        Department.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=xContactMessage.__table__.name
    if thistable.lower() not in existing_tables:
        Department.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=Subscriber.__table__.name
    if thistable.lower() not in existing_tables:
        Subscriber.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=ContactMessage.__table__.name
    if thistable.lower() not in existing_tables:
        ContactMessage.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable = User.__table__.name
    if thistable.lower() not in existing_tables:
        User.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=Role.__table__.name
    if thistable.lower() not in existing_tables:
        Role.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    thistable=Department.__table__.name
    if thistable.lower() not in existing_tables:
        Department.__table__.create(db_engine)
        log_warning("table {0} created in database {1}".format(thistable,DATABASE_NAME))

    existing_tables_after = get_tables_list(db_engine)
    created = 0
    for table in existing_tables_after:
        if table not in existing_tables_before:
            created = created + 1

    log_warning("{0} tables created in database {1}".format(created,DATABASE_NAME))
    log_finish('create_all_tables_manually')

def create_subscribers():
    log_start('create_subscribers')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    #log_info('database-init',  'create default Subscribers')
    created = 0
    users = [
        ('fredericos@leandrou.com', 'Fredericos', 'Leandrou', 'admin')
        ,('philippos@leandrou.com', 'Philippos', 'Leandrou', 'admin')
        ,('spithas@leandrou.com', 'Spithas', 'Leandrou', 'admin')
        ,('admin@leandrou.com', 'admin', 'admin', 'admin')
        ]
    for user in users:
        email = user[0]
        if not Subscriber.query.filter_by(email=email).first():
            thisUser = Subscriber(email=user[0], firstName=user[1], lastName=user[2])
            #db.session.add(thisUser)
            created = created + 1
            log_warning('subscriber created:', thisUser)
    #db.session.commit()
    log_info("{0} Subscribers created in database {1}".format(created, DATABASE_NAME))
    log_finish('create_subscribers')

def create_roles():
    log_start('create_roles')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    created = 0
    if not Role.query.filter_by(name='user').first():
        thisrole = Role(name='user',description='system user')
        db.session.add(thisrole)
        created = created + 1
        log_warning('role created:', thisrole)
    if not Role.query.filter_by(name='sysadmin').first():
        thisrole = Role(name='sysadmin',description='system administrator')
        db.session.add(thisrole)
        created = created + 1
        log_warning('role created:', thisrole)
    if not Role.query.filter_by(name='dbadmin').first():
        thisrole = Role(name='dbadmin',description='database administrator')
        db.session.add(thisrole)
        created = created + 1
        log_warning('role created:', thisrole)
    if not Role.query.filter_by(name='subscriber').first():
        thisrole = Role(name='subscriber',description='subscriber')
        db.session.add(thisrole)
        created = created + 1
        log_warning('role created:', thisrole)
    db.session.commit()
    log_info("{0} Roles created in database {1}".format(created, DATABASE_NAME))
    log_finish('create_roles')

def create_departments():
    log_start('create_departments')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    created = 0
    if not Department.query.filter_by(name='development').first():
        thisDpmt = Department(name='development',description='development')
        db.session.add(thisDpmt)
        created = created + 1
        log_warning('Department created:', thisDpmt)
    if not Department.query.filter_by(name='sales').first():
        thisDpmt = Department(name='sales',description='sales')
        db.session.add(thisDpmt)
        created = created + 1
        log_warning('Department created:', thisDpmt)
    if not Department.query.filter_by(name='administration').first():
        thisDpmt = Department(name='administration',description='administration')
        db.session.add(thisDpmt)
        created = created + 1
        log_warning('Department created:', thisDpmt)
    if not Department.query.filter_by(name='').first():
        thisDpmt = Department(name='',description='subscribers')
        db.session.add(thisDpmt)
        created = created + 1
        log_warning('Department created:', thisDpmt)
    db.session.commit()
    log_info("{0} Departments created in database {1}".format(created, DATABASE_NAME))
    log_finish('create_departments')

def create_users():
    log_start('create_users')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    created = 0
    users = [
        ('fredericos@leandrou.com', 'Fredericos', 'Leandrou', 'admin')
        ,('philippos@leandrou.com', 'Philippos', 'Leandrou', 'admin')
        ,('spithas@leandrou.com', 'Spithas', 'Leandrou', 'admin')
        ,('admin@leandrou.com', 'admin', 'admin', 'admin')
        ]
    for user in users:
        email = user[0]
        if not User.query.filter_by(email=email).first():
            thisUser = User(email=user[0], firstName=user[1], lastName=user[2], roleX=user[3])
            db.session.add(thisUser)
            created = created + 1
            log_warning('user created:', thisUser)
    db.session.commit()
    log_info("{0} Subscribers created in database {1}".format(created, DATABASE_NAME))
    log_finish('create_users')

def list_tables(db_engine):
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    log_info('tables in database:',DATABASE_URI)
    #db_engine = sqlalchemy.create_engine(DATABASE_URI) # connect to database
    existing_tables = db_engine.execute('SHOW TABLES;')
    existing_tables = [d[0] for d in existing_tables]
    t = 0
    for table in existing_tables:
        t = t +1
        log_info("   {0}. {1}.{2}".format(t, DATABASE_NAME,table))
    #db_engine.dispose()

def get_tables_list(db_engine):
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    tables_list = db_engine.execute('SHOW TABLES;')
    tables_list = [d[0] for d in tables_list]
    return tables_list

def init_database():
    log_start('init_database')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI
    log_variable('DATABASE_SERVER_URI', DATABASE_SERVER_URI)
    log_variable('DATABASE_URI', DATABASE_URI)
    create_database()
    create_all_tables_auto()
    create_roles()
    create_departments()
    create_users()
    log_finish('init_database')

#log_finish('application_databases')

if __name__ == '__main__':
    cls() # now, to clear the screen
    init_database()

