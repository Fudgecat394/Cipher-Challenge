#include <iostream>
#include <string>

std::string alphabet = "abcdefghijklmnopqrstuvwxyz";

char decode_chars(char a, char b) {
    int sum_index = (a - 'a') - (b - 'a');
    if (sum_index < 0) sum_index += 26;
    return 'a' + sum_index;
}

std::string decrypt(const std::string& ciphertext, const std::string& key) {
    std::string plaintext = "";
    plaintext.reserve(ciphertext.size());
    int key_index = 0;
    for (int i = 0; i < ciphertext.size(); i++){
        char c = ciphertext[i];
        if (alphabet.find(c) != std::string::npos) {
            char k = key[key_index];
            char t = decode_chars(c, k);
            plaintext += t;
            key_index += 1;
            if (key_index >= key.size()) {
                key_index = 0;
            }

        }
    }
    return plaintext;
}

int main() {
    std::cout << "***********Vigenere Cipher Solver***********" << std::endl;
    std::cout << "Enter the ciphertext: ";
    std::string ciphertext;
    std::cin >> ciphertext;
    std::string key = "a";
    std::string record_key = "";
    std::cout << "Input key: ";
    std::cin >> key;


    std::string plaintext = decrypt(ciphertext, key);

    std::cout << "Decrypted plaintext: " << plaintext << std::endl;

    std::cout << "Press ENTER to exit.";
    std::string exit;
    std::cin >> exit;
}
