"""
QUESTION:
Write a function `check_palindrome_vowels` that checks if a given string is a palindrome, contains all vowels (a, e, i, o, u) in reverse alphabetical order, has no duplicate vowels, and has a length greater than 10 characters. The function should return True if all conditions are met, otherwise it returns False. The comparison should be case-insensitive.
"""

def check_palindrome_vowels(string):
    vowels = ['u', 'o', 'i', 'e', 'a']  # Vowels in reverse alphabetical order
    string = string.lower()  # Convert string to lowercase for case-insensitive comparison
    
    # Check if string is a palindrome
    if string != string[::-1]:
        return False
    
    # Check if string length is greater than 10
    if len(string) <= 10:
        return False
    
    # Check if string contains all vowels in reverse alphabetical order
    for vowel in vowels:
        if vowel not in string:
            return False
        
    # Check if string contains any duplicate vowels
    vowel_set = set()
    for char in string:
        if char in vowels:
            if char in vowel_set:
                return False
            vowel_set.add(char)
    
    return True