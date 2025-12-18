"""
QUESTION:
Create a function named `detect_vowels` that takes a string as input and returns a list of boolean values indicating whether each character in the string is a vowel or not. The function should handle both uppercase and lowercase characters, consider only alphabetic characters, and return False for non-alphabetic characters.
"""

def detect_vowels(string):
    results = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char.isalpha():
            results.append(char.lower() in vowels)
        else:
            results.append(False)
    return results