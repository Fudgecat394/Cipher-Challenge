#Keyword Transposition Cipher Algorithm
untranslated_text = [*input("What is the untranslated text?\n")]
key = [*input("What is the transposition key of the enciphered text? Input the keyword:\n")]
alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
encipher_decipher = input("Are you Enciphering or Deciphering?\n")
for character in range(0, len(key)):
  for letter in range(0, len(alphabet)):
    if key[character] == alphabet[letter]:
      key[character] = letter
for d in range(0, len(key)):
  key[d] = int(key[d])
temp_key = []
sorting_char = 0
swaps = 1
while swaps >0:
  swaps = 0
  while len(temp_key) != len(key):
   temp_key.append(int(key[sorting_char]))
   sorting_char = sorting_char+1
  for counter in range(0,(len(temp_key)-1)):
   if temp_key[counter] > temp_key[counter+1]:
     temp_temp_key = temp_key[counter+1]
     temp_key[counter+1] = temp_key[counter]
     temp_key[counter] = temp_temp_key
     swaps = swaps +1
if encipher_decipher == "Deciphering":
  temporary_key = []
  for q in range(0,len(key)):
    temporary_key.append(key[q])
  for a in range(0,len(key)):
    temporary_key[key[a]-1] = a+1
  key = temporary_key
for i in range(0,len(key)):
  for e in range(0,len(temp_key)):
    if key[i] == temp_key[e]:
      key[i] = e 
for character in range(0,len(untranslated_text)):
  if character == len(untranslated_text):
    break
  elif untranslated_text[character] == " ":
    untranslated_text.remove(" ")
translated_text =[]
for text_letter in range (0,len(untranslated_text),len(key)):
  for num in range(0, len(key)):
    if text_letter + (len(key)) <= len(untranslated_text):
      translated_text.append(untranslated_text[text_letter+key[num]])
    elif text_letter + len(key) > len(untranslated_text):
      while text_letter < len(untranslated_text):
        translated_text.append(untranslated_text[text_letter])
        text_letter = text_letter + 1
      break
print(f"The translated text is: {''.join(translated_text)}")
