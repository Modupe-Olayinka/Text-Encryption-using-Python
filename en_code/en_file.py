from cryptography.fernet import Fernet

key =Fernet.generate_key()

##This is the code to safe the key to a file in a path

#with open('mykey.key', 'wb') as mykey:
#    mykey.write(key)
 
# We open the saved key in mykey.key file path and read it to a variable my_key   
with open('mykey.key', 'rb') as mykey:
    my_key= mykey.read()
    #print(my_key)
    
fernet = Fernet(my_key)
path= 'test.txt' # This is the file path where the text to be encrypted is saved

#open the file path where the text to be encrypted is saved, read and assign to a variable called original
with open(path, 'rb') as original_file:
    original =original_file.read()

#call the fernet class to encrypt the text and assign to a variable named encrypted_original
encrypted_original= fernet.encrypt(original)

#save the encrypted text to a file path named enc_original_txt
with open('enc_original.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_original)
    
path2= 'enc_original.txt'  #This is the file path where the encrypted text to be decrypted is saved

#open the file path where the encrypted text is saved, read and assign to a variable called encrypt
with open(path2,'rb')as encrypt_file:
    encrypt=encrypt_file.read()
    
#call the fernet class to decrypt the text and assign to a variable named decrypted
decrypted= fernet.decrypt(encrypt)

#save the decrypted text to a file path named decrypted.txt
with open('decrypted.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)