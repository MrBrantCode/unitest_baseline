"""
QUESTION:
Write a function `morse_code_translator` that takes a string input and translates it into Morse code, replacing each letter with its Morse code equivalent, separating words with a slash, and representing punctuation marks with double hyphens. The function should support translation of the English alphabet and the period punctuation mark.
"""

def morse_code_translator(input_string):
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '.': '--'}
    morse_code_string = ''
    for char in input_string:
        if char.isalpha():
            morse_code_string += morse_code_dict[char.upper()] + ' '
        elif char == ' ':
            morse_code_string += '/ '
        elif char == '.':
            morse_code_string += morse_code_dict[char] + ' '
    return morse_code_string.strip()