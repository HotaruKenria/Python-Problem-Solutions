# module import
import string
import random

# Function definition
# Parameter - length
def password_generator(length):
  all_chars = string.ascii_letters + string.digits + string.punctuation
  if length < 8:
    print("Password length should be al least 8 character!!!")
    return None
  password = "".join(random.choice(all_chars) for i in range(length))
  return password


# Length input from user
length_password = int(input("Enter the Length for the Password : "))

# Function Call
password_generator(length_password)