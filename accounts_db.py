import sqlite3

conn = sqlite3.connect('accounts.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    account_num INT NOT NULL
);
'''

# cursor.execute(create_table_query)
# cursor.execute("INSERT INTO users (name, login, password, account_num) VALUES (?, ?, ?, ?)", ("Dani stem", "dd1234", "angel", 1))

cursor.execute("SELECT number FROM accounts WHERE number = (select account_num from users where login = 'dd1234')")
all_users = cursor.fetchone()


print("All users in the database:")
# for user in all_users:
clean_data = ''.join(str(all_users))
cleaner_data = clean_data.replace(",","").replace("(","").replace(")","")
print(cleaner_data)



# cursor.execute("INSERT INTO accounts (Number, Owner, Balance) VALUES (?, ?, ?)", (f"{number}", f"{owner}", "0"))


# cursor.execute("SELECT Owner FROM accounts WHERE Number = 1")
# all_users = cursor.fetchall()

# print("All users in the database:")
# for user in all_users:
#     print(user)

conn.commit()

conn.close()
