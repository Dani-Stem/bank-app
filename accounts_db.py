import sqlite3
import bcrypt

conn = sqlite3.connect('accounts.db')

user_input = 'dd1234'
password = user_input.encode('utf-8')
salt = bcrypt.gensalt()
hashed_pass = bcrypt.hashpw(password, salt)
print(f"Hashed password: {hashed_pass}")

cursor = conn.cursor()
cursor.execute("UPDATE users SET password = ? where account_num = 1", (hashed_pass,))
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("All users in the database:")
for user in all_users:
    print(user)


# create_table_query = '''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL UNIQUE,
#     login TEXT NOT NULL,
#     password TEXT NOT NULL,
#     account_num INT NOT NULL
# );
# '''

# cursor.execute(create_table_query)
# cursor.execute("INSERT INTO users (name, login, password, account_num) VALUES (?, ?, ?, ?)", ("Dani stem", "dd1234", "angel", 1))

# cursor.execute("select number from accounts JOIN users on accounts.Number = users.account_num where users.login = 'dd1234'")
# all_users = cursor.fetchone()

# print("All users in the database:")
# # for user in all_users:
# clean_data = int(all_users[0])
# print(clean_data)



# cursor.execute("SELECT Balance FROM accounts WHERE Number = '1'")

# print("All users in the database:")
# all_data = cursor.fetchone()
# clean_data = int(all_data[0])
# print(all_data)
# print(clean_data)
# conn.commit()

# cursor.execute("INSERT INTO accounts (Number, Owner, Balance) VALUES (?, ?, ?)", (f"{number}", f"{owner}", "0"))

# cursor.execute("SELECT Owner FROM accounts WHERE Number = 1")
# all_users = cursor.fetchall()

# print("All users in the database:")
# for user in all_users:
#     print(user)

conn.commit()

conn.close()
