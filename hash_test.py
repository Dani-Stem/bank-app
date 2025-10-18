import bcrypt

user_input = input("Enter Password: ")
password = user_input.encode('utf-8')
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print(f"Hashed password: {hashed_password}")

is_correct = bcrypt.checkpw(test, hashed_password)
print(f"Verification (correct password): {is_correct}")
