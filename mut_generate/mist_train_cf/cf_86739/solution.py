"""
QUESTION:
Implement a recursive function `is_palindrome(s)` that takes a string `s` as input and returns "true" if the string is a palindrome (ignoring non-alphanumeric characters and case sensitivity) and "false" otherwise. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in functions or libraries to reverse the string or check for palindromes.
"""

def is_palindrome(s):
    s = s.lower()
    
    def is_alphanumeric(c):
        return c.isalpha() or c.isdigit()
    
    def check_palindrome(start, end):
        if start >= end:
            return True
        
        if not is_alphanumeric(s[start]):
            return check_palindrome(start + 1, end)
        elif not is_alphanumeric(s[end]):
            return check_palindrome(start, end - 1)
        
        if s[start] == s[end]:
            return check_palindrome(start + 1, end - 1)
        else:
            return False
    
    return check_palindrome(0, len(s) - 1)