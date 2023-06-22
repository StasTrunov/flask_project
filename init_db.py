import sqlite3

connection = sqlite3.connect('themost.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO houses (title, topic, content) VALUES (?, ?, ?)",
            ('Самий дорогий будинок на воді у свиті', 'Будинки на воді', '')
            )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()