import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT
);
'''

# cursor.execute(create_table_query)
# cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ("Alice", "password", "HR@mail.com"))

cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("All users in the database:")
for user in all_users:
    print(user)

conn.commit()

conn.close()
