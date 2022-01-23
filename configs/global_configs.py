app_name = 'mysql-test'
app_version = '1.0.0'
port = 8000
host = '0.0.0.0'

db_name= 'testdb'
db_uri = 'mysql+pymysql://root:praveen1123@localhost/%s?charset=utf8' %db_name
db_uri_empty = 'mysql+pymysql://root:praveen1123@localhost'