# CaesarCypher.py
# Created by Logan-proj
 My second pyhton project has three functions:
   
    0 - Encrypts a message using the ceaser cypher
          Encryption with Caesar code shifts the letters in the alphabet by a chosen shift number
          Example a shift of 3:
          Plain Alphabet:	      ABCDEFGHIJKLMNOPQRSTUVWXYZ#       Caesar Alphabet: (+3)	DEFGHIJKLMNOPQRSTUVWXYZABC

    1 - Decrypts an encrypted message using a known shift key
          Decryption works the inverse way of encryption. The letters in the alphabet are shifted backwards by the same 
          shift number used to encrypt the message

    2 - Decrypts an ecnrypted message using a brute force attack method (no need for a shift key)
          The brute force decryption function runs through all passible shift numbers (1-25) to decrypt each word in the 
          message and then checks the decrypted word against a list of ~ 25,000 english words and only prints the 
          message(s) that matches 20% or more of the word list. 
          This prevents from having to look at all 25 ppossible combinations.
