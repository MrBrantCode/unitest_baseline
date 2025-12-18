"""
QUESTION:
Write a function named `convert_to_morse` that takes a string as input and returns the Morse code equivalent of the string. The function should handle uppercase and lowercase letters (case-insensitive), numbers, and the following special characters: comma, period, question mark, space, hyphen, left parenthesis, and right parenthesis. The Morse code for each character should be separated by a space and the Morse code for each word should be separated by a forward slash (/). The function should return an empty string if the input string is empty.
"""

def convert_to_morse(sentence):
    morse_code_dict = {
                        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                        'Y': '-.--', 'Z': '--..',
                        
                        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                        '8': '---..', '9': '----.',
                        
                        ',': '--..--', '.': '.-.-.-', '?': '..--..', ' ': '/',
                        '-': '-....-', '(': '-.--.', ')': '-.--.-'
                      }

    sentence = sentence.upper()
    morse_code = ""

    for char in sentence:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "

    return morse_code