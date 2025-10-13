import sqlite3

conn = sqlite3.connect('accounts.db')

cursor = conn.cursor()

# create_table_query = '''
# CREATE TABLE IF NOT EXISTS accounts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Number INT NOT NULL UNIQUE,
#     Owner TEXT NOT NULL,
#     Balance INT
# );
# '''

# cursor.execute(create_table_query)
# cursor.execute("INSERT INTO accounts (Number, Owner, Balance) VALUES (?, ?, ?)", ("0001", "Dani Stem", "1000"))

# cursor.execute("SELECT * FROM accounts")
# all_users = cursor.fetchall()

# print("All users in the database:")
# for user in all_users:
#     print(user)



# cursor.execute("INSERT INTO accounts (Number, Owner, Balance) VALUES (?, ?, ?)", (f"{number}", f"{owner}", "0"))


cursor.execute("SELECT Owner FROM accounts WHERE Number = 1")
all_users = cursor.fetchall()

print("All users in the database:")
for user in all_users:
    print(user)

conn.commit()

conn.close()
