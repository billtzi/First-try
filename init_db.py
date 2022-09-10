import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="first_try",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('create table users (user_id serial not null primary key, e_mail varchar(40) unique, name varchar(20), password varchar(20))'
                                 )

# Insert data into the table

cur.execute('INSERT INTO users (e_mail, name, password)'
            'VALUES (%s, %s, %s)',
            ('bill09adam01@gmail.com   ',
             'billtzi',
             '.root.')
            )

conn.commit()

cur.close()
conn.close()