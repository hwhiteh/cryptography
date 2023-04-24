from cryptography.fernet import Fernet
import os
cwd = os.getcwd()

# Read the key file
with open(os.path.join(cwd, "code" , "keyMaon.key"), "rb") as key_file:
    key = key_file.read()

# Read the encrypted code
with open(os.path.join(cwd, "code", "my_script.encrypted"), "rb") as encrypted_file:
    encrypted_code = encrypted_file.read()

# Decrypt the code using the key
cipher = Fernet(key)
decrypted_code = cipher.decrypt(encrypted_code)

# Execute the decrypted code
exec(decrypted_code)
