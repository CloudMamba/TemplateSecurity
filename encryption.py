from Crypto.Cipher import AES
# create new instance of cipher
# from Crypto.Random import get_random_bytes
# key = get_random_bytes(16)
# encryption key
key = b'C&F)H@McQfTjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce


def encryption(dt):
    data = dt.encode()
    # encrypt the data
    ciphertext = cipher.encrypt(data)

    return ciphertext


def decrypt(ciphertext):
    # cipher = AES.new(key, AES.MODE_EAX, nonce)
    # data = cipher.decrypt_and_verify(ciphertext, tag)
    # generate new instance with the key and nonce same as encryption cipher
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # decrypt the data
    plaintext = cipher.decrypt(ciphertext)
    print("Plain text:", plaintext)
    return plaintext
