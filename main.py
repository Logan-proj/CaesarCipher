pip install english-words #imports list of english words > used in brute force dycrytion funtion.
from english_words import english_words_set
import string
alphabet = (string.ascii_lowercase * 2)
shift_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print("------------------------------------")
print("Python Ceasar Cypher Encoder/Decoder")
print("------------------------------------")

#Encryption/Decryption *****
def caesar_funtion(user_input, input_message, shift):
  
  output_message = ""
  for char in input_message:
    if char in alphabet:
      position = alphabet.find(char)
      if user_input == 0:
        new_position = (position + shift)
      elif user_input == 1:
        new_position = (position - shift)
      new_char = alphabet[new_position]
      output_message += new_char
    else:
      output_message += char
  print(f"Message: {output_message}")

#Brute force decryption *****
def brute_force_decryption_function(input_message):

  input_message = str(input_message).lower()
  
  for num in shift_numbers:
    shift = num
    output_message = ""
    for char in input_message:
      if char in alphabet:
        position = alphabet.find(char)
        new_position = (position - shift)
        new_char = alphabet[new_position]
        output_message += new_char
      else:
        output_message += char
    
    list1 = list(output_message.split(" "))
    truelist = []
  #Checks each decrypted word against a list of english words
    for word in list1:
      if word in english_words_set:
        truelist.append("true")
        if len(truelist) > float(len(list1) * .2):
          #Prints out possible message based on how many english words where found
          print(f"Possible message with shift of {shift}:\n** {output_message} **\n")
          break
  
#Front page options *****
def front_page():
  
  user_input = int(input("\nEnter 0 for Encryption\nEnter 1 for Decryption\nEnter 2 for Brute force decryption\n: "))
  input_message = input("Enter message: ").lower()
  
  if user_input == 0 or user_input == 1:
    shift = int(input("Enter shift: "))
    shift = shift % 26
    caesar_funtion(user_input, input_message, shift)
  elif user_input == 2:
    print("\n# Brute force decryption function works best with more words\n")
    brute_force_decryption_function(input_message)
  else:
    print(f"{user_input} Invalid input")
    return

#Loops program untill user exits
should_continue = True
while should_continue:
  front_page()
  result = input("Run program again? Type Y for yes or N for no: ").lower()
  if result == "n":
    should_continue = False
    print("\nGoodbye")
