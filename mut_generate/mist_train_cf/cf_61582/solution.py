"""
QUESTION:
Create a function `check_second_vowel` that takes an array of strings as input. The function should return `True` if any string in the array has the character 'e' at the second position, and `False` otherwise.
"""

def check_second_vowel(array):
    for word in array:
        # We need to check only words with more than 1 character
        if len(word) > 1 and word[1] == 'e':
            return True
    return False