"""
QUESTION:
Write a function named 'helloWorld' that takes a string as input and returns the string with all vowels replaced by the corresponding vowel's next letter in the alphabet. The function should preserve the case of the original letters. The vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).
"""

def helloWorld(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for char in string:
        if char.lower() in vowels:
            next_vowel = chr(ord(char) + 1)
            new_string += next_vowel
        else:
            new_string += char
    return new_string