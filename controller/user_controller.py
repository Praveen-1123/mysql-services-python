from db.db_init import db_engine
from services.response import *

def createUser(body):
    try:
        insert_query = "INSERT INTO Users (id, name, email) VALUES ('{}', '{}', '{}')".format(body['id'], body['name'], body['email'])
        response = db_engine.execute(insert_query)
        get_query = "SELECT * FROM Users WHERE id= {}".format(body['id'])
        response = db_engine.execute(get_query)
        data = response.fetchall()
        if not data:
            return ReF("No user found")
        else:
            return ReS([dict(row) for row in data])
    except:
        return ReF("Unknown Error")

def getUser(user_id):
    try:
        query = "SELECT * FROM Users WHERE id= {}".format(user_id)
        response = db_engine.execute(query)
        data = response.fetchall()
        if not data:
            return ReF("No user found")
        else:
            return ReS([dict(row) for row in data])
    except:
        return ReF("Unknown Error")
