"""
QUESTION:
Design a function `count_vowels(string)` that takes a string as input and returns a dictionary with the frequency of each vowel in the string. The string can contain both uppercase and lowercase letters and has a maximum length of 10^6 characters. The function should not use any built-in string manipulation or regular expression libraries.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in string:
        char = char.lower()
        if char in vowels:
            vowels[char] += 1
    
    return vowels