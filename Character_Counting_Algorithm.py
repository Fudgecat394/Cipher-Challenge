#Character Counting Algorithm
alphabet = [["A", 0], ["B", 0], ["C", 0], ["D", 0 ], ["E", 0], ["F", 0], ["G", 0], ["H", 0 ], ["I", 0], ["J", 0], ["K", 0], ["L", 0], ["M", 0], ["N", 0], ["O", 0], ["P", 0], ["Q", 0], ["R", 0], ["S", 0 ], ["T", 0], ["U", 0], ["V", 0], ["W", 0], ["X", 0], ["Y", 0], ["Z", 0]]
character_count = 0
cipher_text = input("What is the cipher text?\n")
for character in range(len(cipher_text)):
  if cipher_text[character] != " ":
    character_count = character_count + 1
  for letter in range(len(alphabet)):
    if cipher_text[character] == alphabet[letter][0]:
      alphabet[letter][1] = alphabet[letter][1] + 1
      break
for letter in range(len(alphabet)):
  print(f"{alphabet[letter][0]} percentage in text = {((alphabet[letter][1])/character_count)*100}%")
print(f"The number of characters in this text is {character_count}")