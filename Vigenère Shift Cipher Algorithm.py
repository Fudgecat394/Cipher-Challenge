# Vigenère Shift Cipher Algorithm
alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_case_alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encipher_decipher = input("Are you Enciphering or Deciphering this text?\n")
cipher_alphabet = [*input("What is the cipher alphabet?\n")]
key = [*input("What is the key?\n")]
key_count = 0
cipher_alphabet_vigenere = []
cipher_alphabet_temp = []
cipher_text = [*input("what is the cipher text?\n")]
lower_case = input("Are you translating with lower case? Yes or No\n")
spaces = input("Are you translating with spaces? Yes or No\n")
for num in range(0,len(key)):
  if num >= len(key):
    break
  for char in range(0,26):
    cipher_alphabet_temp = []
    cipher_alphabet_temp.append(cipher_alphabet[((char+1)%26)-1])
    if key[num] == cipher_alphabet_temp[0]:
      cipher_alphabet_temp = []
      temp_shift = char
      while len(cipher_alphabet_temp) <26:
        cipher_alphabet_temp.append(cipher_alphabet[((temp_shift+1)%26)-1])
        temp_shift = temp_shift+1
      cipher_alphabet_vigenere.append(cipher_alphabet_temp)
      cipher_alphabet_temp=[]
      break
if lower_case == "Yes" and encipher_decipher == "Enciphering":
  for lower_case_key in range(0,len(cipher_alphabet_vigenere)):
    for capital_letter in range(0,len(cipher_alphabet_vigenere[lower_case_key])):
      for lower_case_letter in range(0,len(lower_case_alphabet)):
        if cipher_alphabet_vigenere[lower_case_key][capital_letter] == alphabet[lower_case_letter]:
          cipher_alphabet_vigenere[lower_case_key][capital_letter] = lower_case_alphabet[lower_case_letter]
if encipher_decipher == "Deciphering":
  for character in range(len(cipher_text)):
    for enciphered_letter in range(len(cipher_alphabet)):
     if cipher_text[character] == cipher_alphabet_vigenere[key_count][enciphered_letter]:
       if lower_case == "Yes":
        cipher_text[character] = lower_case_alphabet[enciphered_letter]
        key_count = (key_count+1)%(len(key))
        break
       else:
        cipher_text[character] = alphabet[enciphered_letter]
        key_count = (key_count+1)%(len(key))
        break
     elif cipher_text[character] == " " and spaces == "No":
        cipher_text[character] = ""
        break
  print(f"The translated text is: {''.join(cipher_text)}" )
if encipher_decipher == "Enciphering":
  for character in range(len(cipher_text)):
    for enciphered_letter in range(len(cipher_alphabet)):
      if cipher_text[character] == alphabet[enciphered_letter]:
        if lower_case == "Yes":
          cipher_text[character] = cipher_alphabet_vigenere[key_count][enciphered_letter]
          key_count = (key_count+1)%(len(key))
          break
        else:
          cipher_text[character] = cipher_alphabet_vigenere[key_count][enciphered_letter]
          key_count = (key_count+1)%(len(key))
          break
      elif cipher_text[character] == " " and spaces == "No":
        cipher_text[character] = ""
        break
  print(f"The translated text is: {''.join(cipher_text)}" )