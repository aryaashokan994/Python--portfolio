import random
import string

print("=== Password Generator ===")

length = int(input("Enter the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Your password is:", password)