# We import the necessary modules
import string # To access alphabetic and numeric characters
import random # To generate random numbers and characters
import secrets # To generate more secure numbers and characters

# We define the length of the password (you can change it according to your preference)
length = 12

# We define the set of characters that can be used in the password
caracteres = string.ascii_letters + string.digits + string.punctuation

# We create an empty list to store the password characters
password = []

# We add at least one character of each type (lowercase, uppercase, number and special) to the password
password.append(random.choice(string.ascii_lowercase)) # We add a lowercase
password.append(random.choice(string.ascii_uppercase)) # We added a capital letter
password.append(random.choice(string.digits)) # We add a number
password.append(random.choice(string.punctuation)) # We added a special character

# We complete the password with random characters until we reach the desired length.
while len(password) < length:
  password.append(secrets.choice(caracteres)) # We use secrets.choice for added security

# We mix up the password characters to avoid predictable patterns
random.shuffle(password)

# We convert the list of characters into a string
password = "".join(password)

# We print the generated password
print("Your password is:", password)