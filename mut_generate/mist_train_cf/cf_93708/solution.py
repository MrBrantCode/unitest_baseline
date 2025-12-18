"""
QUESTION:
Create a function named `convert_to_morse` that takes a string as input, ignores non-alphabetic characters, capitalizes vowels, converts consonants to Morse code, and returns the resulting string with a time complexity of O(n), where n is the length of the input string.
"""

def convert_to_morse(string):
    morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    result = ""
    
    for char in string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                result += char.upper()
            else:
                result += morse_code[char.lower()]
    
    return result