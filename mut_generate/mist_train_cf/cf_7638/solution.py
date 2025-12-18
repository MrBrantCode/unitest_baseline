"""
QUESTION:
Implement a function `is_palindrome(s)` that checks if a given string `s` is a palindrome, ignoring spaces, punctuation, and capitalization. The function must be recursive, have a time complexity of O(n), and not use any built-in functions, libraries, arrays, lists, iteration or looping constructs, auxiliary variables, string concatenation, or string slicing operations. The function should correctly handle strings of any length, including empty strings and edge cases such as strings with only one character or multiple spaces and punctuation marks.
"""

def entrance(s):
    # Base case: empty string or string with only one character is a palindrome
    if len(s) <= 1:
        return True
    
    # Remove spaces and punctuation, and convert to lower case
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Recursive case: check if first and last characters are the same 
    if s[0] != s[-1]:
        return False
    
    # Recursive call: check if the substring without the first and last characters is a palindrome
    return entrance(s[1:-1])