import string

lowercase_letters = list(string.ascii_lowercase)

# User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
original_text = input("Enter the text: ").lower()  # Convert to lowercase for consistency
shift_amount = int(input("Enter the shift value: "))

# Encryption function
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in lowercase_letters:  # Check if it's a letter
            shifted_index = (lowercase_letters.index(letter) + shift_amount) % len(lowercase_letters)
            cipher_text += lowercase_letters[shifted_index]
        else:
            cipher_text += letter  # Keep spaces and special characters unchanged
    return cipher_text

# Decryption function
def decrypt():
    encoded_result = encrypt(original_text, shift_amount)
    print(f" its your encode result {encoded_result}")
    cipher_decode = ""
    for letter in encoded_result:
        if letter in lowercase_letters:  # Check if it's a letter
            shifted_index = (lowercase_letters.index(letter) - shift_amount) % len(lowercase_letters)
            cipher_decode += lowercase_letters[shifted_index]
        else:
            cipher_decode += letter  # Keep spaces and special characters unchanged
    return cipher_decode

# Call the appropriate function based on user input
if direction == "encode":
    encoded_result = encrypt(original_text, shift_amount)
    print(f"Encoded text: {encoded_result}")

elif direction == "decode":
    decoded_result = decrypt()
    print(f"Decoded text: {decoded_result}")

else:
    print("Invalid input! Please type 'encode' or 'decode'.")
