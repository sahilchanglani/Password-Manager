import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



def encrypt(master, newPass):
    
    master = bytearray(master, "utf8")

    newPassByte = bytes(newPass, "utf8")

    salt = "q4j@shq#3n$$bs75@#^&nqj%^%4!!62asdcxoyhkm3*7asdc@`~"
    salt = bytes(salt, "utf8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master))
    f = Fernet(key)
    encrypted_password = f.encrypt(newPassByte)
    encrypted_password = str(encrypted_password)[2:-1]
    salt = str(salt)[2:-1]

    return [encrypted_password,salt]



def decrypt(encrypted_password, master, salt):
    encrypted_password = bytes(encrypted_password, "utf8")
    salt = bytes(salt, "utf8")
    master = bytearray(master, "utf8")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master))
    f = Fernet(key)

    try:
        decMessage = f.decrypt(encrypted_password).decode()
    except:
        return False
    
    return decMessage

