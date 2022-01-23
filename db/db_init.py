from main import app
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from configs.global_configs import *

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy instance
db = SQLAlchemy(app)
ma = Marshmallow(app)

engine = create_engine(db_uri_empty)

db_create = "CREATE DATABASE IF NOT EXISTS %s;" % db_name
engine.execute(db_create)

db_engine = create_engine(db_uri)

db.create_all()
db.session.commit()