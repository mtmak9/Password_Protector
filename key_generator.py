from cryptography.fernet import Fernet

key = Fernet.generate_key()

fkey = open('key_cipher.txt','wb')
fkey.write(key)
print(key)
print('Cipher key generated, key_cipher.txt has been created.\n')