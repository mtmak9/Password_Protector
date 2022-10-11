# Password Protector

A program to encrypt a text file and all content.
The application uses encryption from a cryptographic library.
With this program, you can encrypt any information in a text file that can only be decrypted by this application,
it is a perfect solution for delicate information such as passwords, logins or sensitive data that we would not like to be included in them
hands. The application is simple and has basic functions arranged in such a way that the program does not block access.
If a program for some reason loses access to encryption files or passwords, I have file decoding programs that will decrypt the content if the program has lost access to them.

## Instruction
The default password is 0000

Explanation of individual options:
1. Open File - opens the encrypted file by decrypting it and opening it, when closing the file, the file is encrypted again. (enc_file.txt -> file.txt -> enc_file.txt)
2. Close File - Forces closing and encrypting a file if for some reason it could not be done, or there is an error in the application. (file.txt -> enc_file.txt)
3. Password - Ability to change the application access password to another one

	1. Encrypt Password - Password encryption if it has been decoded in a file (key.txt -> enc_key.txt)

	2. Decrypt Password - Password decryption if it has been / is encoded in a file (enc_key.txt -> key.txt)

	3. Change Password - Change the password to another: (enc_key.txt -> key.txt -> Possibility to edit the file and save 		
	the new password in the notepad)

	4. Back - Return to the previous menu and encrypt the password file (key.txt -> enc_key.txt -> exit)
4. Encryption
	1. Encryption File - Master File Encryption in case of problems (optional)
	2. Decryption File - Main file decryption in case of problems (optional)
	3. Back - return to the previous options

## Program support:

The program is very easy to use, when you run the application to access it, you must enter the password, if the password is correct, you will gain access to all
application function, if the password is incorrect, the application will be closed after 3 attempts.

After entering the correct password, we can open our encrypted file with option no: 1.
We edit the file by. of our own free will and write it with the function of the notebook and close the notebook. The file will be automatically encrypted after you close it.
Then we can exit the application by selecting option 5, the program will check again if the file requires encryption and the application will be closed.

## WARNING!
Do not delete any text files from the folder as they are needed for the proper functioning of the application, if any of the files is deleted the program
will lose access to the main file and all content may be lost.

The file "enc_file.txt" saves all the content hidden in the application, if this file is lost, the content cannot be recovered, if you lose any of the other files,
you can contact me for file decoding programs with which it is possible to recover the contents of an encoded file.

## Application design
![alt_text](https://github.com/mtmak9/Password_Protector/blob/Projects/PPF_screen.png)
