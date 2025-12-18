"""
QUESTION:
Create two functions, `english_to_morse(string)` and `morse_to_english(string)`, that convert a given string of English characters to Morse code and vice versa, respectively. The input string for `english_to_morse(string)` may contain numbers, special characters, and spaces, but should not exceed 100 characters in length. The functions should treat upper and lower case characters as the same, remove consecutive spaces from the input string, and separate each Morse code representation with a space.
"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def entrance(string):
    string = string.upper()
    string = string.strip()  # Remove leading and trailing spaces
    string = ' '.join(string.split())  # Remove consecutive spaces

    morse_code = ''
    for char in string:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '

    return morse_code.strip()