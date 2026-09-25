#Shift Cipher Algorithm
alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cipher_text = [*input("What is the cipher text?\n")]
shift = int(input("What is the shift number?\n"))
spaces = input("Do you want to translate with or without spaces? Yes or No\n")
for character in range(len(cipher_text)):
  for letter in range(len(alphabet)):
    if cipher_text[character] == alphabet[letter]:
      cipher_text[character] = alphabet[((letter +shift+1)
      %26)-1]
      break
    elif cipher_text[character] == " " and spaces == "No":
      cipher_text[character] = ""
text = ''.join(cipher_text)
print(text)
