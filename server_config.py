# myServer/server_config.py
#1 #2 #3 #4 #5 #6 #7 #8 #9 #10 #11 #12 #shalimar
import os
from website_app.debug_services.debug_log_services import *
log_module_start('server_configuration')
################################################################
DISPLAY_CONFIGURATION = False
################################################################
### Secret key for signing cookies
################################################################
SECRET_KEY = 'server-aeiotheosomegasgeometreip9Bv<3Eid9%$i01bobbistarr'
SECURITY_PASSWORD_SALT = 'server-aeiotheosomegasgeometreip9Bvtispaolasbobbistarr'
################################################################
config_file = os.path.abspath(__file__)
config_filename = os.path.basename(__file__)
config_path = os.path.abspath(os.path.dirname(__file__))
APPLICATION_BASEFOLDER = config_path
config_base_folder = os.path.dirname(config_path)
config_folder = config_file.replace(config_filename, '').replace(APPLICATION_BASEFOLDER, '')
################################################################
log_variable('__file__',__file__)
log_variable('config_file', config_file)
log_variable('config_path', config_path)
log_variable('config_folfer', config_folder)
log_variable('config_filename', config_filename)
log_variable('config_base_folder', config_base_folder)
#####################################################################
APPLICATION_BASEFOLDER = config_path #will be used in other configs as the base
os.environ["APPLICATION_BASEFOLDER"] = APPLICATION_BASEFOLDER
SERVER_CONFIG_FILE = config_file
SERVER_CONFIG_PATH = config_path
SERVER_CONFIG_BASE_FOLDER = config_base_folder
SERVER_CONFIG_FOLDER = config_folder
SERVER_CONFIG_FILENAME = config_filename
#####################################################################
EYECATCH = 'SERVER'
#####################################################################
company_name = os.environ.get('COMPANY_NAME', 'LeandrouTechnologyForward')
application_name = os.environ.get('APPLICATION_NAME', 'WEBSITE')
#####################################################################
#os.environ[company_name+'_'+application_name+'_'+'EXECUTION_ENVIRONMENT']='pythonanywhere'
#####################################################################
log_start('server.ini')

EXECUTION_ENVIRONMENT = os.environ.get('EXECUTION_ENVIRONMENT')
if not EXECUTION_ENVIRONMENT:
    EXECUTION_ENVIRONMENT = 'localhost'
SERVER = os.environ.get('DATABASE_SERVER')
EXECUTION_MODE = os.environ.get('EXECUTION_MODE')
MAIL_SERVER_PROVIDER = os.environ.get('MAIL_SERVER_PROVIDER', 'GOOGLE')
GOOGLE_RECAPTCHA_SITE_KEY = os.environ.get('GOOGLE_RECAPTCHA_SITE_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY')
GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY = os.environ.get('GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY')
GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY')

log_variable('EXECUTION_ENVIRONMENT', EXECUTION_ENVIRONMENT)
log_variable('SERVER', SERVER)
log_variable('EXECUTION_MODE', EXECUTION_MODE)
log_variable('GOOGLE_RECAPTCHA_SITE_KEY', GOOGLE_RECAPTCHA_SITE_KEY)
log_variable('GOOGLE_RECAPTCHA_SECRET_KEY', GOOGLE_RECAPTCHA_SECRET_KEY)
log_variable('GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY', GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY)
log_variable('GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY', GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY)

log_finish('server.ini')
#####################################################################
if EXECUTION_ENVIRONMENT == 'localhost':
    if not SERVER:
        SERVER = 'localhost'
    if not EXECUTION_MODE:
        EXECUTION_MODE = 'design'
else:
    if EXECUTION_ENVIRONMENT == 'pythonanywhere':
        if not SERVER:
            SERVER = 'pythonanywhere-ifestionas'
        if not EXECUTION_MODE:
            EXECUTION_MODE = 'production'
    else:
        if not SERVER:
            SERVER = 'pythonanywhere-ganimedes'
        if not EXECUTION_MODE:
            EXECUTION_MODE = 'testing'
log_variable('&&&&&&&&& ENVI', EXECUTION_ENVIRONMENT)
log_variable('&&&&&&&&& SERVER', SERVER)
log_variable('&&&&&&&&& MODE', EXECUTION_MODE)
################################################################
### mail servers
################################################################
MAILJET_MAIL_SERVER = 'in-v3.mailjet.com'
MAILJET_MAIL_PORT = '587' 
# Port 25 or 587 (some providers block port 25). If TLS on port 587 doesn't work, try using port 465 and/or using SSL instead
MAILJET_MAIL_USE_TLS = 'True'
MAILJET_MAIL_USE_SSL = 'True'
MAILJET_MAIL_USERNAME = 'f8d33207c3c7a1ecaf2f74e809b57786'
MAILJET_MAIL_PASSWORD = '2d6a3c2de41ff45b5435382f3e267580'
MAILJET_MAIL_APIKEY_PUBLIC ='f8d33207c3c7a1ecaf2f74e809b57786'
MAILJET_MAIL_APIKEY_PRIVATE ='2d6a3c2de41ff45b5435382f3e267580'

YANDEX_MAIL_SERVER = "smtp.yandex.ru"
YANDEX_MAIL_PORT = '587'
YANDEX_MAIL_USE_TLS = 'True'
YANDEX_MAIL_USE_SSL = 'True'
YANDEX_MAIL_USERNAME = '...' #without the @yandex.ru
YANDEX_MAIL_PASSWORD = '***'
YANDEX_MAIL_APIKEY_PUBLIC = '...'
YANDEX_MAIL_APIKEY_PRIVATE = '...'

GOOGLE_MAIL_SERVER = "smtp.gmail.com"
GOOGLE_MAIL_PORT = '587'
GOOGLE_MAIL_USE_TLS = 'False'
GOOGLE_MAIL_USE_SSL = 'True'
GOOGLE_MAIL_USERNAME = 'akamas2020@gmail.com'
GOOGLE_MAIL_PASSWORD = 'philea13'
GOOGLE_MAIL_USERNAME = 'bstarr131@gmail.com'
GOOGLE_MAIL_PASSWORD = 'bstarr13'
GOOGLE_MAIL_USERNAME = 'spithas@leandrou.com'
GOOGLE_MAIL_PASSWORD = 'spithas3116'
GOOGLE_MAIL_APIKEY_PUBLIC = '...'
GOOGLE_MAIL_APIKEY_PRIVATE = '...'

if MAIL_SERVER_PROVIDER == 'MAILJET':
    MAIL_SERVER = MAILJET_MAIL_SERVER
    MAIL_PORT = MAILJET_MAIL_PORT
    MAIL_USE_TLS = MAILJET_MAIL_USE_TLS
    MAIL_USE_SSL = MAILJET_MAIL_USE_SSL
    MAIL_USERNAME = MAILJET_MAIL_USERNAME
    MAIL_PASSWORD = MAILJET_MAIL_PASSWORD
    MAIL_APIKEY_PUBLIC = MAILJET_MAIL_APIKEY_PUBLIC
    MAIL_APIKEY_PRIVATE = MAILJET_MAIL_APIKEY_PRIVATE
else:
    if MAIL_SERVER_PROVIDER == 'YANDEX':
        MAIL_SERVER = YANDEX_MAIL_SERVER
        MAIL_PORT = YANDEX_MAIL_PORT
        MAIL_USE_TLS = YANDEX_MAIL_USE_TLS
        MAIL_USE_SSL = YANDEX_MAIL_USE_SSL
        MAIL_USERNAME = YANDEX_MAIL_USERNAME
        MAIL_PASSWORD = YANDEX_MAIL_PASSWORD
        MAIL_APIKEY_PUBLIC = YANDEX_MAIL_APIKEY_PUBLIC
        MAIL_APIKEY_PRIVATE = YANDEX_MAIL_APIKEY_PRIVATE
    else:
        MAIL_SERVER = GOOGLE_MAIL_SERVER
        MAIL_PORT = GOOGLE_MAIL_PORT
        MAIL_USE_TLS = GOOGLE_MAIL_USE_TLS
        MAIL_USE_SSL = GOOGLE_MAIL_USE_SSL
        MAIL_USERNAME = GOOGLE_MAIL_USERNAME
        MAIL_PASSWORD = GOOGLE_MAIL_PASSWORD
        MAIL_APIKEY_PUBLIC = GOOGLE_MAIL_APIKEY_PUBLIC
        MAIL_APIKEY_PRIVATE = GOOGLE_MAIL_APIKEY_PRIVATE
################################################################
### databases connection
################################################################
#dialect+driver://username:password@host:port/database

#localhost
# DATABASE_SERVER = 'localhost'
# DATABASE_NAME = 'ifestionas_db'

# DATABASE_SERVER_URI = 'mysql+pymysql://ganimedes:philea13@localhost'
# DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME

DATABASE_HOST_ADDRESS = 'ganimedes.mysql.pythonanywhere-services.com'
DATABASE_USER = 'ganimedes'
DATABASE_PASS = 'philea13'
DATABASE_NAME = 'ganimedes$ganimides_db'

DATABASE_HOST_ADDRESS = 'localhost'
DATABASE_NAME = 'ifestionas_db'
DATABASE_USER = 'ganimedes'
DATABASE_PASS = 'philea13'
DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
DATABASE_SERVER = DATABASE_HOST_ADDRESS
DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME
localhost_SQLALCHEMY_DATABASE_URI = DATABASE_URI


#ganimedes database on pythonanywhere
DATABASE_HOST_ADDRESS = 'ganimedes.mysql.pythonanywhere-services.com'
DATABASE_USER = 'ganimedes'
DATABASE_PASS = 'philea13'
DATABASE_NAME = 'ganimedes$ganimides_db'
DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
DATABASE_SERVER = DATABASE_HOST_ADDRESS
DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME
pythonanywhere_ganimedes_SQLALCHEMY_DATABASE_URI = DATABASE_URI

#ifestionas database on pythonanywhere
DATABASE_HOST_ADDRESS = 'ifestionas.mysql.pythonanywhere-services.com'
DATABASE_USER = 'ifestionas'
DATABASE_PASS = 'philea13'
DATABASE_NAME = 'ifestionas$ganimides_db'
DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
DATABASE_SERVER = DATABASE_HOST_ADDRESS
DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME
pythonanywhere_ifestionas_SQLALCHEMY_DATABASE_URI = DATABASE_URI

pythonanywhere_SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ifestionas:philea13@ifestionas.mysql.pythonanywhere-services.com/ifestionas$ganimides_db'
pythonanywhere_SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimides:philea13@ganimides.mysql.pythonanywhere-services.com/ganimides$ganimides_db'

#localhost_SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimedes:philea13@localhost/ifestionas_db'
#localhost_SQLALCHEMY_TEST_DATABASE_URI = 'mysql+pymysql://ganimedes:philea13@localhost/ganimedes_db_test'

DATABASE_HOST_ADDRESS = 'localhost'
DATABASE_USER = 'ganimedes'
DATABASE_PASS = 'philea13'
DATABASE_NAME = 'ifestionas_db'
DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
DATABASE_SERVER = DATABASE_HOST_ADDRESS
DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME

if EXECUTION_ENVIRONMENT == 'pythonanywhere':
    DATABASE_HOST_ADDRESS = 'ganimedes.mysql.pythonanywhere-services.com'
    DATABASE_USER = 'ganimedes'
    DATABASE_PASS = 'philea13'
    DATABASE_NAME = 'ganimedes$ganimides_db'
    DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
    DATABASE_SERVER = DATABASE_HOST_ADDRESS
    DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
    DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME
    if SERVER == 'pythonanywhere-ifestionas':
        DATABASE_HOST_ADDRESS = 'ifestionas.mysql.pythonanywhere-services.com'
        DATABASE_USER = 'ifestionas'
        DATABASE_PASS = 'philea13'
        DATABASE_NAME = 'ifestionas$ganimides_db'
        DATABASE_CONNECTION_PREFIX = 'mysql+pymysql://'
        DATABASE_SERVER = DATABASE_HOST_ADDRESS
        DATABASE_SERVER_URI = DATABASE_CONNECTION_PREFIX+DATABASE_USER+':'+DATABASE_PASS+'@'+DATABASE_HOST_ADDRESS
        DATABASE_URI = DATABASE_SERVER_URI+'/'+DATABASE_NAME

################################################
# SQLALCHEMY
################################################
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_POOL_RECYCLE = 10
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 60 #less than SQLALCHEMY_POOL_RECYCLE
SQLALCHEMY_POOL_RECYCLE = 100 #greater than SQLALCHEMY_POOL_TIMEOUT
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#SQLALCHEMY_MAX_OVERFLOW = 5
#SQLALCHEMY_POOL_RECYCLE = 90
#SQLALCHEMY_POOL_TIMEOUT = 90
#SQLALCHEMY_POOL_SIZE = 5
#SQLALCHEMY_POOL_RECYCLE = -1
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# mysql> show global variables like "wait_timeout";
# +---------------+-------+
# | Variable_name | Value |
# +---------------+-------+
# | wait_timeout  | 300   |
# +---------------+-------+
# 1 row in set (0.00 sec)
# mysql> show global variables like "%timeout%";
# +-----------------------------+----------+
# | Variable_name               | Value    |
# +-----------------------------+----------+
# | connect_timeout             | 10       |
# | delayed_insert_timeout      | 300      |
# | have_statement_timeout      | YES      |
# | innodb_flush_log_at_timeout | 1        |
# | innodb_lock_wait_timeout    | 50       |
# | innodb_rollback_on_timeout  | OFF      |
# | interactive_timeout         | 28800    |
# | lock_wait_timeout           | 31536000 |
# | net_read_timeout            | 30       |
# | net_write_timeout           | 60       |
# | rpl_stop_slave_timeout      | 31536000 |
# | slave_net_timeout           | 60       |
# | wait_timeout                | 300      |
# +-----------------------------+----------+
# 13 rows in set (0.01 sec)
#SQLALCHEMY_POOL_SIZE = 5
#SQLALCHEMY_POOL_TIMEOUT = 60
################################################
# '''
# pool_recycle=-1: this setting causes the pool to recycle
#     connections after the given number of seconds has passed. It
#     defaults to -1, or no timeout. For example, setting to 3600
#     means connections will be recycled after one hour. Note that
#     MySQL in particular will disconnect automatically if no
#     activity is detected on a connection for eight hours (although
#     this is configurable with the MySQLDB connection itself and the
#     server configuration as well).
# '''
# #    "charset": "utf8"
# #}
# import pymysql
# connection = pymysql.connect(host='***',
#                                  user='***',
#                                  password='***',
#                                  db='***',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor
#                                  )

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimedes:philea13@localhost/ganimides_db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimides:philea13@ganimides.mysql.pythonanywhere-services.com/ganimides$ganimides_db'
# #print('      ', SERVER_CONFIG_FOLDER, SERVER_CONFIG_FILE, '###instance### ###config.py### SQLALCHEMY_DATABASE_URI=',SQLALCHEMY_DATABASE_URI)
# username = "ganimides"
# password = "philea13"
# hostname = "ganimides.mysql.pythonanywhere-services.com"
# databasename = "ganimides$ganimides_db"
# database_username = "ganimides"
# database_password = "spithas13"
# SQLALCHEMY_DATABASE_URI2 = "mysql+{mysqlconnector}://{username}:{password}@{hostname}/{databasename}".format(
#     mysqlconnector="pymysql",
#     username="ganimides",
#     password="philea13",
#     hostname="ganimides.mysql.pythonanywhere-services.com",
#     databasename="ganimides$ganimides_db"
# )
# #db = SQLAlchemy(app, engine = create_engine("mysql+myqldb://ganimides:philea13@ganimides.mysql.pythonanywhere-services.com/ganimides$ganimides_db", pool_recycle=280))
# #mysql://InsulT:password@mysql.server/InsulT$default'
# #{
# #    "host": "localhost",
# #    "user": "root",
# #    "password": "philea13",
# #    "database": "db",
# #    "sql_engine": "mysql+pymysql",
# #    "charset": "utf8"
# #}
# #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# #DATABASE_CONNECT_OPTIONS = {}

################################################################
### ipstack access key
################################################################
IPSTACK_API_ACCESSKEY = '4022cfd2249c3431953ecf599152892e'
IPSTACK_URL = 'http://api.ipstack.com/'

################################################################
### recaptcha config
################################################################
localhost_GOOGLE_RECAPTCHA_SITE_KEY = "6LcD3XkUAAAAABAoO2p4WOoBGg6uRyCoVCcGNCFV"
localhost_GOOGLE_RECAPTCHA_SECRET_KEY = "6LcD3XkUAAAAAHTNpV8RsDN8CybCNEJ0htRddCMq"
localhost_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY = "6LfL2HkUAAAAAF8ot-2aPAHYzHPAAxvLtKI-PyXi"
localhost_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY = "6LfL2HkUAAAAAIdjgyCwgSaV2hvOS6APpoXot1yw"

localhost_XXXXXX_RECAPTCHA_SITE_KEY = "6LcD3XkUAAAAABAoO2p4WOoBGg6uRyCoVCcGNCFV"
localhost_XXXXXX_RECAPTCHA_SECRET_KEY = "6LcD3XkUAAAAAHTNpV8RsDN8CybCNEJ0htRddCMq"
localhost_XXXXXX_RECAPTCHA_INVISIBLE_SITE_KEY = "6LfL2HkUAAAAAF8ot-2aPAHYzHPAAxvLtKI-PyXi"
localhost_XXXXXX_RECAPTCHA_INVISIBLE_SECRET_KEY = "6LfL2HkUAAAAAIdjgyCwgSaV2hvOS6APpoXot1yw"

pythonanywhere_GOOGLE_RECAPTCHA_SITE_KEY = "6LeQxnwUAAAAAAyscnSdBS0RbNo6BEDje-trtOV-"
pythonanywhere_GOOGLE_RECAPTCHA_SECRET_KEY = "6LeQxnwUAAAAAGjxVdpUGhRREi5xQQQhRfROJCmZ"
pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY = "...."
pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY = "..."

pythonanywhere_XXXXXX_RECAPTCHA_SITE_KEY = "6LeQxnwUAAAAAAyscnSdBS0RbNo6BEDje-trtOV-"
pythonanywhere_XXXXXX_RECAPTCHA_SECRET_KEY = "6LeQxnwUAAAAAGjxVdpUGhRREi5xQQQhRfROJCmZ"
pythonanywhere_XXXXXX_RECAPTCHA_INVISIBLE_SITE_KEY = "...."
pythonanywhere_XXXXXX_RECAPTCHA_INVISIBLE_SECRET_KEY = "..."

if GOOGLE_RECAPTCHA_SITE_KEY and GOOGLE_RECAPTCHA_SECRET_KEY:
    # from server.ini
    RECAPTCHA_SITE_KEY = GOOGLE_RECAPTCHA_SITE_KEY
    RECAPTCHA_SECRET_KEY = GOOGLE_RECAPTCHA_SECRET_KEY
    RECAPTCHA_INVISIBLE_SITE_KEY = GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY
    RECAPTCHA_INVISIBLE_SECRET_KEY = GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY
else:
    if EXECUTION_ENVIRONMENT == 'pythonanywhere':
        RECAPTCHA_SITE_KEY = pythonanywhere_GOOGLE_RECAPTCHA_SITE_KEY
        RECAPTCHA_SECRET_KEY = pythonanywhere_GOOGLE_RECAPTCHA_SECRET_KEY
        RECAPTCHA_INVISIBLE_SITE_KEY = pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY
        RECAPTCHA_INVISIBLE_SECRET_KEY = pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY
    else:
        RECAPTCHA_SITE_KEY = localhost_GOOGLE_RECAPTCHA_SITE_KEY
        RECAPTCHA_SECRET_KEY = localhost_GOOGLE_RECAPTCHA_SECRET_KEY
        RECAPTCHA_INVISIBLE_SITE_KEY = localhost_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY
        RECAPTCHA_INVISIBLE_SECRET_KEY = localhost_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY

RECAPTCHA_PUBLIC_KEY = RECAPTCHA_SITE_KEY
RECAPTCHA_PRIVATE_KEY = RECAPTCHA_SECRET_KEY
RECAPTCHA_INVISIBLE_PUBLIC_KEY = RECAPTCHA_INVISIBLE_SITE_KEY
RECAPTCHA_INVISIBLE_PRIVATE_KEY = RECAPTCHA_INVISIBLE_SECRET_KEY

################################################################
#store in os.environ in order to be used in instance or app_config
################################################################
os.environ["EXECUTION_ENVIRONMENT"] = EXECUTION_ENVIRONMENT
os.environ["EXECUTION_MODE"] = EXECUTION_MODE
os.environ["SERVER"] = SERVER

os.environ["DATABASE_SERVER"] = DATABASE_SERVER
os.environ["DATABASE_NAME"] = DATABASE_NAME
os.environ["DATABASE_SERVER_URI"] = DATABASE_SERVER_URI
os.environ["DATABASE_URI"] = DATABASE_URI
os.environ["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

os.environ["MAIL_SERVER_PROVIDER"] = MAIL_SERVER_PROVIDER
# os.environ["MAILJET_MAIL_SERVER"] = MAILJET_MAIL_SERVER
# os.environ["MAILJET_MAIL_PORT"] = MAILJET_MAIL_PORT
# os.environ["MAILJET_MAIL_USE_TLS"] = MAILJET_MAIL_USE_TLS
# os.environ["MAILJET_MAIL_USE_SSL"] = MAILJET_MAIL_USE_SSL
# os.environ["MAILJET_MAIL_USERNAME"] = MAILJET_MAIL_USERNAME
# os.environ["MAILJET_MAIL_PASSWORD"] = MAILJET_MAIL_PASSWORD
# os.environ["MAILJET_MAIL_APIKEY_PUBLIC"] = MAILJET_MAIL_APIKEY_PUBLIC
# os.environ["MAILJET_MAIL_APIKEY_PRIVATE"] = MAILJET_MAIL_APIKEY_PRIVATE

# os.environ["YANDEX_MAIL_SERVER"] = YANDEX_MAIL_SERVER
# os.environ["YANDEX_MAIL_PORT"] = YANDEX_MAIL_PORT
# os.environ["YANDEX_MAIL_USE_TLS"] = YANDEX_MAIL_USE_TLS
# os.environ["YANDEX_MAIL_USE_SSL"] = YANDEX_MAIL_USE_SSL
# os.environ["YANDEX_MAIL_USERNAME"] = YANDEX_MAIL_USERNAME
# os.environ["YANDEX_MAIL_PASSWORD"] = YANDEX_MAIL_PASSWORD
# os.environ["YANDEX_MAIL_APIKEY_PUBLIC"] = YANDEX_MAIL_APIKEY_PUBLIC
# os.environ["YANDEX_MAIL_APIKEY_PRIVATE"] = YANDEX_MAIL_APIKEY_PRIVATE

# os.environ["GOOGLE_MAIL_SERVER"] = GOOGLE_MAIL_SERVER
# os.environ["GOOGLE_MAIL_PORT"] = GOOGLE_MAIL_PORT
# os.environ["GOOGLE_MAIL_USE_TLS"] = GOOGLE_MAIL_USE_TLS
# os.environ["GOOGLE_MAIL_USE_SSL"] = GOOGLE_MAIL_USE_SSL
# os.environ["GOOGLE_MAIL_USERNAME"] = GOOGLE_MAIL_USERNAME
# os.environ["GOOGLE_MAIL_PASSWORD"] = GOOGLE_MAIL_PASSWORD
# os.environ["GOOGLE_MAIL_APIKEY_PUBLIC"] = GOOGLE_MAIL_APIKEY_PUBLIC
# os.environ["GOOGLE_MAIL_APIKEY_PRIVATE"] = GOOGLE_MAIL_APIKEY_PRIVATE

# os.environ["MAIL_SERVER"] = MAIL_SERVER
# os.environ["MAIL_PORT"] = MAIL_PORT
# os.environ["MAIL_USE_TLS"] = MAIL_USE_TLS
# os.environ["MAIL_USE_SSL"] = MAIL_USE_SSL
# os.environ["MAIL_USERNAME"] = MAIL_USERNAME
# os.environ["MAIL_PASSWORD"] = MAIL_PASSWORD
# os.environ["MAIL_APIKEY_PUBLIC"] = MAIL_APIKEY_PUBLIC
# os.environ["MAIL_APIKEY_PRIVATE"] = MAIL_APIKEY_PRIVATE

# os.environ["localhost_SQLALCHEMY_DATABASE_URI"] = localhost_SQLALCHEMY_DATABASE_URI
# os.environ["pythonanywhere_SQLALCHEMY_DATABASE_URI"] = pythonanywhere_SQLALCHEMY_DATABASE_URI

# os.environ["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

# os.environ["localhost_GOOGLE_RECAPTCHA_SITE_KEY"] = localhost_GOOGLE_RECAPTCHA_SITE_KEY
# os.environ["localhost_GOOGLE_RECAPTCHA_SECRET_KEY"] = localhost_GOOGLE_RECAPTCHA_SECRET_KEY
# os.environ["localhost_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY"] = localhost_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY
# os.environ["localhost_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY"] = localhost_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY

# os.environ["pythonanywhere_GOOGLE_RECAPTCHA_SITE_KEY"] = pythonanywhere_GOOGLE_RECAPTCHA_SITE_KEY
# os.environ["pythonanywhere_GOOGLE_RECAPTCHA_SECRET_KEY"] = pythonanywhere_GOOGLE_RECAPTCHA_SECRET_KEY
# os.environ["pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY"] = pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY
# os.environ["pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY"] = pythonanywhere_GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY

os.environ["RECAPTCHA_SITE_KEY"] = RECAPTCHA_SITE_KEY
os.environ["RECAPTCHA_SECRET_KEY"] = RECAPTCHA_SECRET_KEY
os.environ["RECAPTCHA_INVISIBLE_SITE_KEY"] = RECAPTCHA_INVISIBLE_SITE_KEY
os.environ["RECAPTCHA_INVISIBLE_SECRET_KEY"] = RECAPTCHA_INVISIBLE_SECRET_KEY

#############################################################################################
log_info('########################################################')
log_info('# server configuration')
log_info('########################################################')
log_variable('base folder', SERVER_CONFIG_BASE_FOLDER)
log_variable('EXECUTION_ENVIRONMENT', EXECUTION_ENVIRONMENT)
log_variable('EXECUTION_MODE', EXECUTION_MODE)
log_variable('SERVER', SERVER)
log_variable('DATABASE_SERVER', DATABASE_SERVER)
log_variable('DATABASE_NAME', DATABASE_NAME)
log_variable('DATABASE_SERVER_URI', DATABASE_SERVER_URI)
log_variable('DATABASE_URI', DATABASE_URI)
log_variable('SQLALCHEMY_DATABASE_URI', SQLALCHEMY_DATABASE_URI)
log_info('########################################################')
log_variable('MAIL_SERVER_PROVIDER', MAIL_SERVER_PROVIDER)
log_variable('MAIL_SERVER', MAIL_SERVER)
log_variable('MAIL_PORT', MAIL_PORT)
log_variable('MAIL_USE_TLS', MAIL_USE_TLS)
log_variable('MAIL_USE_SSL', MAIL_USE_SSL)
log_variable('MAIL_USERNAME', MAIL_USERNAME)
log_variable('MAIL_PASSWORD', MAIL_PASSWORD)
log_variable('MAIL_APIKEY_PUBLIC', MAIL_APIKEY_PUBLIC)
log_variable('MAIL_APIKEY_PRIVATE', MAIL_APIKEY_PRIVATE)
log_info('########################################################')
log_variable('GOOGLE_RECAPTCHA_SITE_KEY', RECAPTCHA_SITE_KEY)
log_variable('GOOGLE_RECAPTCHA_SECRET_KEY', RECAPTCHA_SECRET_KEY)
log_variable('GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY', RECAPTCHA_INVISIBLE_SITE_KEY)
log_variable('GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY', RECAPTCHA_INVISIBLE_SECRET_KEY)
log_info('########################################################')
log_variable('IPSTACK_API_ACCESSKEY', RECAPTCHA_SITE_KEY)
log_variable('IPSTACK_URL', RECAPTCHA_SECRET_KEY)
log_info('########################################################')
log_variable('SECRET_KEY',SECRET_KEY)
log_variable('SECURITY_PASSWORD_SALT',SECURITY_PASSWORD_SALT)
log_info('########################################################')
log_module_finish('server_configuration')
