from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Read the secret key
with open('secret_key', 'rb') as k:
    key = k.read()

# Read the encrypted shopping cart data
with open('encrypted_cart', 'rb') as dec:
    iv = dec.read(16)
    ciphertext = dec.read()

# Decrypt the file by using same sercet key and CBC Mode with IV
decrypted = AES.new(key, AES.MODE_CBC, iv)

plaintext = unpad(decrypted.decrypt(ciphertext), AES.block_size)

# Decrypt the file into excel file
with open('dcrypted_file.xlsx', 'wb') as df:
    df.write(plaintext)
