from db.db_init import db_engine
from services.response import *

def dropTable(table_name):
    try:
        get_query = 'SHOW TABLES LIKE "%s";' %table_name
        response = db_engine.execute(get_query)
        data = response.fetchall()
        if not data:
            return ReS("Table Not Found")

        delete_query = 'DROP TABLE IF EXISTS {};'.format(table_name)
        response = db_engine.execute(delete_query)
        return ReS("Table Deleted")
    except:
        return ReF("Unknown Error")