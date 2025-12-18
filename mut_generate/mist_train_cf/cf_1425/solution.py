"""
QUESTION:
Write a function named `check_string` that takes a string as input and returns `True` if it consists only of lowercase alphabetic characters and contains at least one vowel. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def check_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Check if the string is empty
    if not string:
        return False
    
    # Check if all characters are lowercase alphabets and contains at least one vowel
    for char in string:
        if not char.islower() or (len(string) == 1 and char not in vowels):
            return False
        if char in vowels:
            break
    else:
        return False
    
    return True