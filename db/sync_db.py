from db.db_init import db_engine

users_table_name = 'Users'

def checkExists():
    print("Called")
    create_query = "CREATE TABLE IF NOT EXISTS %s (id VARCHAR(40) NOT NULL PRIMARY KEY, name  VARCHAR(40), email VARCHAR(40))" %users_table_name
    db_engine.execute(create_query)