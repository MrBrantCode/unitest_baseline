"""
QUESTION:
Create two functions, `english_to_morse` and `morse_to_english`, that can convert English characters to Morse code and vice versa. The functions should handle upper and lower case characters as the same, remove multiple consecutive spaces from the input string, and support the conversion of numbers and special characters. Each Morse code representation should be separated by a space, and the input string should not exceed 100 characters in length.
"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def morse_code_translator(string):
    string = string.upper()
    string = string.strip()  # Remove leading and trailing spaces
    string = ' '.join(string.split())  # Remove consecutive spaces

    if string[0] in MORSE_CODE_DICT:
        morse_code = ''
        for char in string:
            if char in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[char] + ' '

        return morse_code.strip()
    else:
        english_text = ''
        morse_code_list = string.split(' ')
        for code in morse_code_list:
            for key, value in MORSE_CODE_DICT.items():
                if value == code:
                    english_text += key

        return english_text