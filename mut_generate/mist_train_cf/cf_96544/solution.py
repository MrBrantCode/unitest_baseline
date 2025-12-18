"""
QUESTION:
Write a function called `string_to_morse` that takes a string of English characters as input and returns its Morse code representation. The function should handle strings containing numbers, special characters, and spaces, treating upper and lower case characters as the same. It should also remove multiple consecutive spaces in the input string and separate each Morse code representation with a space. The input string should not exceed 100 characters in length.
"""

def string_to_morse(input_string):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
    input_string = input_string.upper()  # Convert to uppercase
    input_string = ' '.join(input_string.split())  # Remove multiple consecutive spaces

    morse_string = ''
    for char in input_string:
        morse_char = morse_code.get(char, '')
        morse_string += morse_char + ' '

    return morse_string.strip()  # Remove trailing space