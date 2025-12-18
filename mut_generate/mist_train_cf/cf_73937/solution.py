"""
QUESTION:
Create a function called `to_morse` that translates English text to Morse code, and another function called `to_char` that translates Morse code back to English text. The translation should consider alphabets, numbers, and special characters. The Morse code translation should use a single space to act as a delimiter between Morse representations of individual characters and a slash("/") to act as delimiter between words.
"""

CHAR_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
                 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                 '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
                 '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
                 ' ': ' ', '!': '-.-.--', '-': '-....-', '(':'-.--.', 
                 ')': '-.--.-', ' ': '/'}

MORSE_TO_CHAR = {morse: char for char, morse in CHAR_TO_MORSE.items()}

def to_morse(s):
    return ' '.join(CHAR_TO_MORSE[c.upper()] for c in s)

def to_char(s):
    return ''.join(MORSE_TO_CHAR[m] for m in s.split())