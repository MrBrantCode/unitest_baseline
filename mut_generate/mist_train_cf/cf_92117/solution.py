"""
QUESTION:
Write a function `is_palindrome_vowels(string)` that checks if a given string is a palindrome and contains all the vowels (a, e, i, o, u) in alphabetical order, ignoring non-alphabetic characters and case differences. The function should return `True` if the string meets these conditions and `False` otherwise.
"""

def is_palindrome_vowels(string):
    # Convert the string to lowercase to handle case-insensitive comparison
    string = string.lower()
    
    # Check if the string is a palindrome
    if string == string[::-1]:
        
        # Check if all vowels are present in the string
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_order = []
        for char in string:
            if char in vowels and char not in vowel_order:
                vowel_order.append(char)
                
                # Check if the vowels are in alphabetical order
                if vowel_order == sorted(vowel_order):
                    continue
                else:
                    return False
        
        # Check if all the vowels are present
        if len(vowel_order) == len(vowels):
            return True
    
    return False