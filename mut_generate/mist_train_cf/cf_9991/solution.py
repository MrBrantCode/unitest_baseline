"""
QUESTION:
Implement a function `replace_vowels` that takes a string and two parameters: a specified letter and a number of positions. The function should replace all vowels in the string with the specified letter, which is obtained by shifting the original vowel's ASCII value by the given number of positions. The function should handle both positive and negative shifts, and preserve the case of the original vowels.
"""

def replace_vowels(s, shift, specified_letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in s:
        if char.lower() in vowels:
            ascii_value = ord(char) + shift
            new_char = chr(ascii_value)
            result += specified_letter.lower() if char.islower() else specified_letter.upper()
        else:
            result += char
    return result