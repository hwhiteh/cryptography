from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Save the key to a file
with open("keyMain.key", "wb") as key_file:
    key_file.write(key)

# Read the code to encrypt
with open("main.py", "rb") as code_file:
    code = code_file.read()

# Encrypt the code using the key
cipher = Fernet(key)
encrypted_code = cipher.encrypt(code)

# Save the encrypted code to a file
with open("my_script.encrypted", "wb")as encrypted_file:
    encrypted_file.write(encrypted_code)
