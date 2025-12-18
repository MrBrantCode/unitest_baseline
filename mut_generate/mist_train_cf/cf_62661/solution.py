"""
QUESTION:
Write a function `translate_to_morse(input_string)` that takes a string of alphanumeric characters and spaces as input, and returns the Morse code translation of the input string. The Morse code for each letter and number should be separated by a space, and each word should be separated by a slash. The function should handle both uppercase and lowercase letters, but the Morse code output should not distinguish between cases.
"""

def translate_to_morse(input_string):
    dictionary_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.' 
    }
    
    input_string = input_string.upper()
    result = ''

    for character in input_string:
        if character in dictionary_morse:
            result += dictionary_morse[character] + ' '
        elif character == ' ':
            result += '/ '
        else:
            result += character + ' '

    return result