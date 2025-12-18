"""
QUESTION:
Create a method named 'helloWorld' that takes a string as input and returns the string with all vowels replaced by the corresponding vowel's next letter in the alphabet, preserving the original case. The method should handle both lowercase and uppercase vowels.
"""

def helloWorld(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for char in string:
        if char.lower() in vowels:
            next_vowel = chr(ord(char) + 1)
            if next_vowel.lower() in vowels:
                if char.isupper():
                    next_vowel = next_vowel.upper()
            new_string += next_vowel
        else:
            new_string += char
    return new_string