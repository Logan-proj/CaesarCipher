# CaesarCipher.py
# Created by Logan-proj
 My second python project has three functions:
   
    0 - Encrypts a message using the Caesar cipher
          Encryption with Caesar code shifts the letters in the alphabet by a chosen shift number
          Example a shift of 3:
          Plain Alphabet:  ABCDEFGHIJKLMNOPQRSTUVWXYZ#  Caesar Alphabet: (+3)	DEFGHIJKLMNOPQRSTUVWXYZABC

    1 - Decrypts an encrypted message using a known shift key
          Decryption works the inverse way of encryption. The letters in the alphabet are shifted 
          backward by the same shift number used to encrypt the message

    2 - Decrypts an encrypted message using a brute force attack method (no need for a shift key)
          The brute force decryption function runs through all possible shift numbers (1-25) to decrypt 
          each word in the message and then checks the decrypted word against a list of ~ 230,000 English 
          words and only prints the message(s) that matches 20% or more of the word list. 
          This prevents from having to look at all 25 possible combinations.
