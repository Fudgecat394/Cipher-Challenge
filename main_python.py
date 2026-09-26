class Text_to_decrypt:
    
    reference_key = "etaoinshrdlcumwfgypbvkjxqz"
    reference_frequencies = [0.127, 0.091, 0.082, 0.075, 0.070, 0.067, 0.063,
            0.061, 0.060, 0.043, 0.040, 0.028, 0.028, 0.024,
            0.024, 0.022, 0.020, 0.020, 0.019, 0.015, 0.010,
            0.0081, 0.0015, 0.0015, 0.00095,  0.00074]
    encrypted_text = ""
    letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
            ]
    frequencies = [
            0,    0,   0,   0,   0,   0,   0,
            0,    0,   0,   0,   0,   0,   0,
            0,    0,   0,   0,   0,   0,   0,
            0,    0,   0,   0,   0
            ]
    errors = []
    letter_str = "abcdefghijklmnopqrstuvwxyz"
    decoding_key = ""
    characters_to_decode = 0
    decoded_text = ""

    def __init__(self):
        self.encrypted_text = input('Enter the encrypted text: ').lower()
        if self.encrypted_text == 'file':
            with open('code.txt') as f:
                self.encrypted_text = (f.readlines()).lower()
        print(self.encrypted_text)

    def get_frequency(self):
        for letter in self.encrypted_text:
            index = self.letter_str.find(letter)
            if index != -1:
                self.frequencies[index] += 1
                self.characters_to_decode += 1

    def generate_key_basic(self):
        for index in range(self.characters_to_decode, -1, -1):
            for i in range(len(self.frequencies)):
                if self.frequencies[i] == index:
                    self.decoding_key += self.letters[i]
                    
    def decrypt_code(self):
        self.decoded_text = ""
        for letter in self.encrypted_text:
            if self.decoding_key.find(letter) == -1:
                self.decoded_text += letter
            else:
                index = self.decoding_key.find(letter)
                self.decoded_text += self.reference_key[index]

        
            
    
            
            

if __name__ == '__main__':
    msg = Text_to_decrypt()
    msg.get_frequency()
    print(msg.frequencies)
    msg.generate_key_basic()
    print(msg.decoding_key)
    
    while True:
        msg.decrypt_code()
        print(msg.decoded_text)
        print(f'Decoding key: {msg.decoding_key}')
        print(f'Reference key: {msg.reference_key}')
        print('What letters to switch? ')
        value1 = input('Choice 1: ')
        value2 = input('Choice 2: ')
        msg.reference_key = msg.reference_key.replace(value1, '*')
        msg.reference_key = msg.reference_key.replace(value2, value1)
        msg.reference_key = msg.reference_key.replace('*', value2)
        
        
                

        
