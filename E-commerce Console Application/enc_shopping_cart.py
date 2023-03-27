from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secrets import token_bytes

# 16 byte key
key = token_bytes(16)

# Create a file to store the secret key
with open('secret_key', 'wb') as k:
    secret_key = k.write(key)

# Cipher by using the 16 byte key with the CBC Mode
cipher = AES.new(key, AES.MODE_CBC)

# Read the shopping cart data
with open('shopping_cart.xlsx', 'rb') as f:
    file = f.read()

encrypted = cipher.encrypt(pad(file, AES.block_size))

# Encrypt the shopping cart data into txt file by using AES
with open('encrypted_cart', 'wb') as enc:
    enc.write(cipher.iv)
    enc.write(encrypted)
