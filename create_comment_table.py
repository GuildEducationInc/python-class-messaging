import sqlite3

with open('comment_schema.txt') as comment_schema:
    with sqlite3.connect('messages.db') as conn:
        conn.execute('DROP TABLE IF EXISTS comments')
        create_sql = comment_schema.read()
        conn.execute(create_sql)


