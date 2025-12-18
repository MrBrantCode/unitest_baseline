"""
QUESTION:
Write a function named `check_anagram_and_palindrome` that takes two strings as input and returns True if they are both anagrams and palindromes, and False otherwise. The function should ignore spaces, punctuation, and capitalization when making this determination.
"""

def check_anagram_and_palindrome(string1, string2):
    # Convert the strings to lowercase and remove spaces and punctuation
    string1 = ''.join(e for e in string1 if e.isalnum()).lower()
    string2 = ''.join(e for e in string2 if e.isalnum()).lower()
    
    # Check if the strings are anagrams
    if sorted(string1) != sorted(string2):
        return False
    
    # Check if the strings are palindromes
    if string1 != string1[::-1] or string2 != string2[::-1]:
        return False
    
    return True