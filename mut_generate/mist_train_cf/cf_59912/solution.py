"""
QUESTION:
Write a function named `string_to_morse` that takes a string as input and returns its Morse code representation. The Morse code mapping is predefined, where a space (' ') separates letters and a slash ('/') separates words. The function should be case-insensitive and should handle both letters and spaces in the input string. The Morse code dictionary is given as: {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}.
"""

# Define dictionary MAP for Morse Code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def string_to_morse(input_string):
    # Create an empty string to hold Morse Code
    morse_code = ''
    for char in input_string.upper():
        if char != " ":
            # Get Morse code of character and add a space
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            # Add a / in Morse code to represent a space
            morse_code += '/ '
    return morse_code