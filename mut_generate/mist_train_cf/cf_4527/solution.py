"""
QUESTION:
Create a function named `check_palindrome_vowels` that takes one string parameter. The function should return True if the input string meets the following conditions and False otherwise: 
- The string is a palindrome.
- The string contains all the vowels 'a', 'e', 'i', 'o', 'u' in reverse alphabetical order.
- The string does not contain any duplicate vowels.
- The string has a length greater than 10 characters.
The function should be case-insensitive.
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
    if len(set(string)) != len(string):
        return False
    
    return True