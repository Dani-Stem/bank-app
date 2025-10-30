import bcrypt
test = "wrongpassword"
user_input = "ab"

password = user_input.encode('utf-8')
salt = bcrypt.gensalt()
print(salt)
hashed_password = bcrypt.hashpw(password, salt)
print(f"Hashed password: {hashed_password}")

is_correct = bcrypt.checkpw(test.encode('utf-8'), hashed_password)
print(f"Verification (correct password): {is_correct}")
