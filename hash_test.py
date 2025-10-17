import bcrypt

# Convert the password to bytes (bcrypt requires byte strings)
password = b"mysecretpassword"

# Generate a salt
salt = bcrypt.gensalt()

# Hash the password
hashed_password = bcrypt.hashpw(password, salt)
print(f"Hashed password: {hashed_password}")

# Verify a correct password
is_correct = bcrypt.checkpw(password, hashed_password)
print(f"Verification (correct password): {is_correct}")

# Verify an incorrect password
incorrect_password = b"wrongpassword"
is_incorrect = bcrypt.checkpw(incorrect_password, hashed_password)
print(f"Verification (incorrect password): {is_incorrect}")