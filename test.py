import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
#zodpovedny sa run query a store the result

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)
