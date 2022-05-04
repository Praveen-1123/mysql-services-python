import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app_name = os.environ.get('APP_NAME') if os.environ.get('APP_NAME') != None else 'mysql-test'
app_version = os.environ.get('APP_VERSION') if os.environ.get('APP_VERSION') != None else '1.0.0'
port = os.environ.get('PORT') if os.environ.get('PORT') != None else 8000
host = os.environ.get('HOST') if os.environ.get('HOST') != None else '0.0.0.0'

db_name = os.environ.get('DB_NAME') if os.environ.get('DB_NAME') != None else 'testdb'
db_uri = os.environ.get('DB_URI') if os.environ.get('DB_URI') != None else 'mysql+pymysql://root:password@localhost/%s?charset=utf8' %db_name
db_uri_empty = os.environ.get('DB_CONNECT') if os.environ.get('DB_CONNECT') != None else 'mysql+pymysql://root:password@localhost'