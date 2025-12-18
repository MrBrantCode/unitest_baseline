"""
QUESTION:
Implement a function called `substitution_cipher` that takes a string `text` and a dictionary `character_map` as input. The function should return the encrypted text by replacing each character in `text` with the corresponding character in `character_map` if it exists, otherwise keep the original character. The `character_map` dictionary contains the substitution rules for lowercase English alphabets, shifting each letter one step forward (e.g., 'a' becomes 'b', 'b' becomes 'c', etc.).
"""

def substitution_cipher(text, character_map):
    output = ""
    for char in text:
        if char in character_map:
            output += character_map[char]
        else:
            output += char
    return output