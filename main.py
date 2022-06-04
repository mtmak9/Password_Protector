import os
from cryptography.fernet import Fernet
#import encryption, decryption, key_generator

attempt = 1
options = 0
options_pass = 0
options_enc = 0
#main_file = 'file.txt'
#-----------------------------------------------------
#Szyfrowanie pliku z hasłem
fkey = open("key_cipher.txt",'rb') #using Cipher from this file
key = fkey.read()
cipher = Fernet(key)
encrypted_pass_file = 'enc_key.txt' #encrypted file

with open(encrypted_pass_file ,'rb') as df:
    encrypted_data = df.read()        
decrypted_file = cipher.decrypt(encrypted_data)
password = decrypted_file.decode('utf-8')
#------------------------------------------------------

def open_file():
    #decryption_main_file
    try:
        decrypt_file()
        #os.system('file.txt')
        print('File open Successfully')
    except:
        print('\nError: missing Encrypted file - enc_file.txt\n')
    encrypt_file()
    
def close_file():
    #def encrypt_file()
    try:
        encrypt_file()
        print('File close Successfully')
    except:
        print('\nError: missing Decrypted file - file.txt\n')
    #close_main_file
    
def encrypt_file():
    fkey = open("key_cipher.txt",'rb') #using Cipher from this file
    key = fkey.read()
    cipher = Fernet(key)
    dec_main_file = 'file.txt' #decrypted file

    with open(dec_main_file, 'rb') as f:
        e_file = f.read()   
    encrypted_file = cipher.encrypt(e_file)
    #Create encrypted file and save it
    with open("enc_" + dec_main_file, 'wb') as ef:
        ef.write(encrypted_file)
    #Delete decrypted file
    os.remove(dec_main_file)
    print('\nEncryption process completed, enc_file.txt has been created.\n')

def decrypt_file():
    #decryption_main_file
    fkey = open("key_cipher.txt",'rb') #using Cipher from this file
    key = fkey.read()
    cipher = Fernet(key)
    enc_main_file = 'enc_file.txt' #encrypted file

    with open(enc_main_file ,'rb') as df:
        encrypted_data = df.read()        
    decrypted_file = cipher.decrypt(encrypted_data)
    
    #Create decrypted file and save it
    with open('file.txt', 'wb') as df:
        df.write(decrypted_file)
    #Delete encrypted file
    os.remove(enc_main_file)
    print('\nDecryption process completed, file.txt has been created.\n')
    #open_main_file
    os.system('file.txt')

def encrypt_password():
    #encryption password
    fkey = open("key_cipher.txt",'rb') #using Cipher from this file
    key = fkey.read()
    cipher = Fernet(key)
    file = 'key.txt' #decrypted file

    with open(file, 'rb') as f:
        e_file = f.read()   
    encrypted_file = cipher.encrypt(e_file)
    
    #Create encrypted file and save it
    with open("enc_" + file, 'wb') as ef:
        ef.write(encrypted_file)
    #Delete decrypted file
    os.remove(file)
    print('Encryption process completed, enc_key.txt has been created.\n')

def decrypt_password():
    #decryption password
    fkey = open("key_cipher.txt",'rb') #using Cipher from this file
    key = fkey.read()
    cipher = Fernet(key)
    file = 'enc_key.txt' #encrypted file

    with open(file ,'rb') as df:
        encrypted_data = df.read()        
    decrypted_file = cipher.decrypt(encrypted_data)
    
    #Create decrypted file and save it
    with open('key.txt', 'wb') as df:
        df.write(decrypted_file)
    #Delete encrypted file
    os.remove(file)
    print('Decryption process completed, key.txt has been created.\n')

while attempt < 4:
    pass_input = input('Type your password: ')
    
    if pass_input == password:
        print('Correct Password\n')
        print('Choose one of the option:\n ')
        
        while options != '5':           
            options = input('\n1.Open File\n2.Close File\n3.Password\n4.Encryption\n5.Exit\nChoose number, one of the option: ')
            
            #---------------------------------------------------------------------------------
            #1.OPEN FILE
            if options == '1':
                open_file()
            #---------------------------------------------------------------------------------    
            #2.CLOSE FILE    
            elif options == '2':
                close_file()
            
            #--------------------------------------------------------------------------------    
            #3.PASSWORD    
            elif options == '3':
                while options_pass != '4': 
                    options_pass = input('\n1.Encrypt Password\n2.Decrypt Password\n3.Change Password\n4.Back\nChoose number, one of the option: ')
                    #1.ENCRYPT PASSWORD
                    if options_pass == '1':
                        try:
                            encrypt_password()
                        except:
                            print('\nError missing file - key.txt\n')
                            
                    #2.DECRYPT PASSWORD
                    elif options_pass == '2':
                        try:
                            decrypt_password()
                        except:
                            print('\nError: missing file - enc_key.txt\n')
                            
                    #3.CHANGE PASSWORD
                    elif options_pass == '3':
                        try:
                            try:
                                decrypt_password()
                            except:
                                pass
                            os.system('key.txt')
                        except:
                            print('\nError: Something went wrong')
                    #4.BACK
                    elif options_pass == '4':
                        try:
                            encrypt_password()
                        except:
                            pass
                        break
            #--------------------------------------------------------------------------------        
            #4.OPTION                            
            elif options == '4':
                while options_enc != '3': 
                    options_enc = input('\n1.Encryption File\n2.Decryption File\n3.Back\nChoose number, one of the option: ')
                    #1.Encryption File
                    if options_enc == '1':
                        encrypt_file()
                    #2.Decryption File    
                    elif options_enc == '2':
                        decrypt_file()
                    #3.Back    
                    elif options_enc == '3':
                        break
            #--------------------------------------------------------------------------------
            #5.EXIT    
            elif options == '5':
                try:
                    encrypt_file()
                except:
                    pass
                break
            #--------------------------------------------------------------------------------
        break        
    else:
        print('Incorrect Password, Try again: ')
        print('Your attempts: ', attempt)
        attempt += 1
        

