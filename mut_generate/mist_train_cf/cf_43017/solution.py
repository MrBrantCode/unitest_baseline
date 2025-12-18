"""
QUESTION:
Create a function `morse` that takes a string `s` as input and returns its Morse code representation as a string. The function should ignore any non-alphabetic characters and separate each Morse code character by a space. The input string can be a mix of uppercase and lowercase letters, but the function should handle them case-insensitively. The output string should not have a trailing space.
"""

def morse(s):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
    }
    s = s.upper()
    morse_str = ''
    for char in s:
        if char.isalpha():
            morse_str += morse_code[char] + ' '
    return morse_str.strip()