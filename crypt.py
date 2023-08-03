import ucryptolib
import ubinascii

class crypt():
    def __init__(self,key):
        self.key = key
        
    def decrypt(self, data):
        if isinstance(data, bytes):
            encrypted_data_bytes = data


            # Create an AES object with the key and mode (ECB)
            aes_obj = ucryptolib.aes(self.key, 1, b"\x00" * 16)

            # Decrypt the data
            decrypted_data = aes_obj.decrypt(encrypted_data_bytes)

            # Remove PKCS#7 padding using the helper function unpad_pkcs7
            def unpad_pkcs7(data):
                pad_length = data[-1]
                return data[:-pad_length]

            data_to_decrypt = unpad_pkcs7(decrypted_data)
            data = data_to_decrypt.decode()
            return data
        else:
            raise ValueError("data should be in a form bytes")

    def encrypt(self, data):
        if isinstance(data, str):
            data_to_encrypt = data.encode()

            # Pad the data to a multiple of 16 bytes using PKCS#7 padding
            block_size = 16
            padding_length = block_size - (len(data_to_encrypt) % block_size)
            padded_data = data_to_encrypt + bytes([padding_length]) * padding_length

            # Create an AES object with the key and mode (ECB)
            aes_obj = ucryptolib.aes(self.key, 1, b"\x00" * 16)

            # Encrypt the data
            encrypted_data = aes_obj.encrypt(padded_data)
            return encrypted_data
        else:
            raise ValueError("data should be in a form of STR.")
