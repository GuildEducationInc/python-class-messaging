import sqlite3

with open('dbschema.txt') as dbschema:
    with sqlite3.connect('messages.db') as conn:
        create_sql = dbschema.read()
        conn.execute(create_sql)

