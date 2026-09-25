#include <iostream>
#include <string> 
#include <vector>

const std::string reference_key = "etaoinshrdlcumwfgypbvkjxqz";

const std::vector<float> reference_frequencies = {
	0.127, 0.091, 0.082, 0.075, 0.070, 0.067, 0.063,
	0.061, 0.060, 0.043, 0.040, 0.028, 0.028, 0.024,
	0.024, 0.022, 0.020, 0.020, 0.019, 0.015, 0.010,
	0.0081, 0.0015, 0.0015, 0.00095,  0.00074
};

float abs(float n){
	if (n < 0) return n * -1;
	else return n;
};


class Text_to_decrypt
{
public:
	std::string encrypted_text = "";

	std::vector<char> letters = {
		'a', 'b', 'c', 'd', 'e', 'f', 'g',
		'h', 'i', 'j', 'k', 'l', 'm', 'n',
		'o', 'p', 'q', 'r', 's', 't', 'u',
		'v', 'w', 'x', 'y', 'z'
    };
	std::vector<float> frequencies = {
		0,    0,   0,   0,   0,   0,   0,
		0,    0,   0,   0,   0,   0,   0,
		0,    0,   0,   0,   0,   0,   0,
		0,    0,   0,   0,   0
    };
	std::vector<float> errors = {};
	std::string letter_str = { "abcdefghijklmnopqrstuvwxyz" };
	std::string decoding_key = "";
	int characters_to_decode = 0;
	std::string decoded_text = "";

	Text_to_decrypt() {
		std::cout << "\nEnter the encrypted text: ";
		std::getline(std::cin, encrypted_text);
		std::cout << encrypted_text << std::endl;
	}

	void get_frequency() {
        int N = encrypted_text.length();

		for (int i = 0; i < N; i++) {
			char c = encrypted_text[i];
			int index = letter_str.find(c);
            frequencies[index] ++;
		}

        for (int i = 0; i < frequencies.size(); i++){
            std::cout << frequencies[i] << std::endl;
			characters_to_decode += frequencies[i];
        }
		std::cout << "Total characters to decode: " << characters_to_decode << std::endl;
	};

	void generate_key_basic(){
		for (int i = characters_to_decode; i > 0; i--){
			for (int iterate = 0; iterate < frequencies.size(); iterate++){
            	if (i==frequencies[iterate]){
					decoding_key += letter_str[iterate];
				}
			}
		}
	}
	void decrypt_code(){
		for (int i = 0; i < encrypted_text.size(); i++){
			if (decoding_key.find(encrypted_text[i]) == std::string::npos){
				decoded_text += encrypted_text[i];
			}
			else {
				int index = decoding_key.find(encrypted_text[i]);
				decoded_text += reference_key[index];
			}
		}
	}
	void calculate_key_error(){
		for (int i = 0; i < decoding_key.size(); i++){
			char letter = decoding_key[i];
			int index = letter_str.find(letter);
			float frequency = frequencies[index] / characters_to_decode;

			float reference_frequency = reference_frequencies[i];

			float error_range = 1-frequency/reference_frequency;

			errors.push_back(error_range);

			std::cout << "Error for the decryption " << letter << " to " << reference_key[i] << " is " << error_range * 100 << "%" << std::endl;
		}
	}
	int get_weakest_correlation(){
		float largest_error_bound = 0;
		int largest_error_index = 0;
		for (int i = 0; i < errors.size() - 1; i++){
			float error_bound = - errors[i] +  errors[i+1];
			std::cout << "Error bound at " << i << " is " << error_bound << std::endl;
			if (error_bound < largest_error_bound) largest_error_bound = error_bound, largest_error_index = i;
		};
		std::cout << largest_error_bound << " Found at index " << largest_error_index << std::endl;

		return largest_error_index;
	};

	void switch_weakest(int index){
		char value_1 = decoding_key[index];
		char value_2 = decoding_key[index+1];
		decoding_key[index] = value_2;
		decoding_key[index+1] = value_1;
		errors = {};
	}


};


int main() {

	std::cout << "**************Decryptor**************\n";
	Text_to_decrypt msg = Text_to_decrypt();
	msg.get_frequency();
	msg.generate_key_basic();

	int accuracy = 0;

	while (accuracy < 10){
	msg.calculate_key_error();
	std::cout << "Accuracy: " << std::endl;
	std::cin >> accuracy;
	int index = msg.get_weakest_correlation();
	msg.switch_weakest(index);
	}
	
	//msg.decrypt_code();
	std::cout << msg.decoding_key << std::endl;
	std::cout << msg.decoded_text << std::endl;
    std::string exit;
    std::cin >> exit;
	return 0;
}