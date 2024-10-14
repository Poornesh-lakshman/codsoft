import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print(f"Generated password: {password}")


