from cryptography.fernet import Fernet
import os

fkey = open("key_cipher.txt",'rb') #using Cipher from this file
key = fkey.read()
cipher = Fernet(key)
file = 'key.txt' #decrypted file

def f_encryption():
    with open(file, 'rb') as f:
        e_file = f.read()   
    encrypted_file = cipher.encrypt(e_file)
    
    #Create encrypted file and save it
    with open("enc_" + file, 'wb') as ef:
        ef.write(encrypted_file)
    #Delete decrypted file
    os.remove(file)
    print('Encryption process completed, enc_key.txt has been created.\n')
f_encryption()