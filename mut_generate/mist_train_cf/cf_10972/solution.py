"""
QUESTION:
Create a function `encode_to_morse` that converts a given string to Morse code. The function should:

- Validate the input string and only allow alphanumeric characters, spaces, and return an error message if any invalid characters are found.
- Handle both uppercase and lowercase letters by converting them to lowercase before encoding.
- Include the Morse code representation for each valid character, including numbers and special characters.
- Represent multiple words with a slash (/) in the Morse code.
- Return the Morse code representation as a string with each character or word on a separate line is not required but the Morse code for each word should be separated by a slash.

The function should use the following Morse code dictionary:
'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
"""

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def encode_to_morse(text):
    encoded_text = ""
    for char in text:
        if char.lower() not in morse_code:
            print(f"Invalid character: {char}")
            return None
        encoded_text += morse_code[char.lower()] + " "
    return encoded_text.strip()