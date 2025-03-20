import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return None

    password = ""
    for _ in range(length):
        choice = random.randint(1, 3)  # 1 for letter, 2 for digit, 3 for special character

        if choice == 1:  # Add a random letter (uppercase or lowercase)
            password += random.choice(string.ascii_letters)
        elif choice == 2:  # Add a random digit
            password += random.choice(string.digits)
        else:  # Add a random special character
            password += random.choice(string.punctuation)

    return password

# Generate a password of length 12
generated_password = generate_password(12)
print("Generated Password:", generated_password)
