from cryptography.fernet import Fernet
import os

fkey = open("key_cipher.txt",'rb') #using Cipher from this file
key = fkey.read()
cipher = Fernet(key)
file = 'enc_key.txt' #encrypted file

def f_decryption():
    with open(file ,'rb') as df:
        encrypted_data = df.read()        
    decrypted_file = cipher.decrypt(encrypted_data)
    
    #Create decrypted file and save it
    with open('key.txt', 'wb') as df:
        df.write(decrypted_file)
    #Delete encrypted file
    os.remove(file)
    print('Decryption process completed, key.txt has been created.\n')
f_decryption()