# For Example to use this Program on ESP32 or any Micropython-Board

from crypt import crypt
import os
key = os.urandom(16) #It will 128 bits AES key

c = crypt(key)

plain_text = "Hello World"
print("Plain Message : ",plain_text)

#to Encrypt Data
encrypted_text = c.encrypt(plain_text)
print("Encrypted Message : ",encrypted_text)

#to Decrypt Data
decrypted_text = c.decrypt(encrypted_text)
print("Decrypted Message : ",decrypted_text)