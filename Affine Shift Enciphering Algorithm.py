#Affine Shift Cipher Algorithm
alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cipher_alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
multiplication_key = int(input("What is the multiplication key?\n"))
addition_key = int(input("What is the addition key\n"))
text_choice = input("Would you like the translated text? Yes or No\n")
alphabet_choice = input("Do you want the alphabet,Yes or No?\n")
if alphabet_choice == "Yes":
  for letter in range(len(alphabet)):
    new=(((((letter+1)*multiplication_key)+addition_key)%26)-1)
    cipher_alphabet[letter]=alphabet[new]
  print(f"The alphabet used by the translated text would be {''.join(cipher_alphabet)}")
if text_choice == "Yes":
  text = [*input("what is the text?\n")]
  spaces = input("Would you like to translate with spaces or not? Yes or No\n")
  for character in range(len(text)):
    for letter in range(len(alphabet)):
      if text[character] == alphabet[letter]:
        text[character] = alphabet[((((letter+1)*multiplication_key)+addition_key)%26)-1]
        break
      elif text[character] == " " and spaces == "No":
        text[character] = ""
        break
  print(f"The translated text is: {''.join(text)}" )