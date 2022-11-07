from urllib import parse

HOSTNAME = '117.78.1.34'
PORT = '26000'
DATABASE = 'db_hwork'
USERNAME = 'user_hwork'
PASSWORD = 'user_hwork@1234'
PASSWORD = parse.quote_plus(PASSWORD)
DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
DEBUG = True

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
