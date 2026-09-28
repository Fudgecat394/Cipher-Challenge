#include <iostream>
#include <string>

std::string alphabet = "abcdefghijklmnopqrstuvwxyz";

char decode_chars(char a, char b) {
    int sum_index = (a - 'a') - (b - 'a');
    if (sum_index < 0) sum_index += 26;
    return 'a' + sum_index;
}

int decrypt(const std::string& ciphertext, const std::string& key) {
    int key_index = 0;
    int score = 0;
    bool t_found = false;
    bool th_found = false;
    bool tha_found = false;

    bool w_found = false;
    bool wo_found = false;
    bool wou_found = false;
    bool woul_found = false;

    for (int i = 0; i < ciphertext.size(); i++){
        char c = ciphertext[i];
        if (c >= 'a' && c <= 'z') {
            char k = key[key_index];
            char t = decode_chars(c, k);
            if (tha_found && t == 't'){
                score += 1;
                t_found = false;
                th_found = false;
                tha_found = false;
            } else if (t_found && t == 'h'){
                th_found = true;
            } else if (th_found && t == 'a'){
                tha_found = true;
            } else if (t == 't'){
                t_found = true;
            } else {
                t_found = false;
                th_found = false;
                tha_found = false;
            }
            if (t == 'w'){
                w_found = true;
            } else if (w_found && t == 'o'){
                wo_found = true;
            } else if (wo_found && t == 'u'){
                wou_found = true;
            } else if (wou_found && t == 'l'){
                woul_found = true;
            } else if (woul_found && t == 'd'){
                score += 1;
                w_found = false;
                wo_found = false;
                wou_found = false;
                woul_found = false;
            } else {
                w_found = false;
                wo_found = false;
                wou_found = false;
                woul_found = false;
            }

            key_index += 1;
            if (key_index >= key.size()) {
                key_index = 0;
            }

        }
    }
    return score;
}

int main() {
    std::cout << "***********Vigenere Cipher Solver***********" << std::endl;
    std::cout << "Enter the ciphertext: ";
    std::string ciphertext;
    std::cin >> ciphertext;
    std::string key = "a";
    int record_es = 0;
    std::string record_key = "";


    while (key!="zzzzzzzz"){
        int score = decrypt(ciphertext, key);

        if (score >= record_es){
            record_es = score;
            record_key = key;
            std::cout << "New record key: " << record_key << " With score: " << score << "\n";
        }
        for (int i = key.size() - 1; i >= 0; i--){
            char current_char = key[i];
            if (current_char == 'z'){
                if (i == 0){
                    key += 'a';
                    //std::cout << "Current key: " << key << "\n";
                }  
                key[i] = 'a';
            } else {
                key[i] = alphabet[alphabet.find(current_char) + 1];
                break;
            }
        }

    }
}