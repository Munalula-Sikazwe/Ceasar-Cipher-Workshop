### This is the cipher_alphabet of supported characters

cipher_alphabet = " abcdefghijklmnopqrstuvwxyz"

###
shift_key = 23
#### Encryption function
def encrypt(plaintext):
    
    cipher_text =''
    
    plaintext = plaintext.lower()
    
    for letter in plaintext:
        
        index = cipher_alphabet.find(letter)
        
        ### implementing the encryption algorithm which is is E n(x)= (x+n)mod/length of the alphabet    
        index = (index+shift_key)%len(cipher_alphabet)
        
        ### replace the letter in the plaintext with the cipher letter using the new shifted index
        cipher_text +=  cipher_alphabet[index] 
        
    return cipher_text

result = encrypt("This is an Example")
print(result)
  #### Decryption funtion 

def decrypt(ciphertext):
    
    decrypted_text =''
    
    ciphertext = ciphertext.lower()
    
    for letter in ciphertext:
        
        index = cipher_alphabet.find(letter)
        
        
        index = (index-shift_key)%len(cipher_alphabet)
        
        
        decrypted_text +=  cipher_alphabet[index] 
        
    return decrypted_text

decrypted_text = decrypt(result)

print(decrypted_text)