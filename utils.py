import csv
import os
from cryptography.fernet import Fernet
import hashlib

# account management
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hashed_password, entered_password):
    hashed_entered = hash_password(entered_password)
    
    return hashed_entered == stored_hashed_password

# entries
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher_suite = Fernet(key)

