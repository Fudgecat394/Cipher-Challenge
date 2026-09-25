# Monoalphabetic Substitution Cipher Algorithm
alphabet = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_case_alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
temp_alphabet = []
encipher_decipher = input("Enciphering or Deciphering?\n")
cipher_alphabet = [*input("What is the cipher alphabet?\n")]
untranslated_text = [*input("what is the untranslated text?\n")]
spaces = input("Would you like to translate with spaces? Yes or No\n")
lower_case = input("Are you translating with lower case? Yes or No\n")
if encipher_decipher == "Enciphering":
  temp_alphabet = alphabet
  alphabet = cipher_alphabet
  cipher_alphabet = temp_alphabet
  for i in range(len(alphabet)):
    lower_case_alphabet[i] = alphabet[i].lower()
for character in range(len(untranslated_text)):
  for letter in range(len(cipher_alphabet)):
    if untranslated_text[character] == cipher_alphabet[letter]:
      if lower_case == "Yes":
        untranslated_text[character] = lower_case_alphabet[letter]
        break
      else:
        untranslated_text[character] = alphabet[letter]
        break
    elif untranslated_text[character] == " " and spaces == "No":
      untranslated_text[character] = ""
      break
print(f"The translated text is: {''.join(untranslated_text)}" )