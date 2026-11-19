def space_remover():
    untranslated_text = [*input("What is the untranslated text?\n")]
    for character in range(0, len(untranslated_text)):
        if character == len(untranslated_text):
            break
        elif untranslated_text[character] == " ":
            untranslated_text.remove(" ")
    return untranslated_text
text = space_remover()
new_text = []
key_length = int(input("What is the length of the key?\n"))
for character in range(0, 2112, (2112//key_length)):
    new_text.append(text[character])
    print(character)
print(new_text)
