"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome. The function should ignore non-alphanumeric characters and consider case insensitivity. It must have a time complexity of O(n), where n is the length of the input string, and cannot use built-in functions or libraries to reverse the string or check for palindromes. The function should be implemented recursively.
"""

def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Initialize two pointers, one at the beginning of the string and one at the end
    start = 0
    end = len(s) - 1
    
    # Helper function to check if a character is alphanumeric
    def is_alphanumeric(c):
        return c.isalpha() or c.isdigit()
    
    # Recursive function to check if the string is a palindrome
    def check_palindrome(start, end):
        # Base case: if the start pointer is greater than or equal to the end pointer,
        # the entire string has been checked and is a palindrome
        if start >= end:
            return True
        
        # If the characters at the start and end pointers are not alphanumeric,
        # move the pointers inward and check again
        if not is_alphanumeric(s[start]):
            return check_palindrome(start + 1, end)
        elif not is_alphanumeric(s[end]):
            return check_palindrome(start, end - 1)
        
        # If the characters at the start and end pointers are equal, move the pointers inward
        # and check the substring between them
        if s[start] == s[end]:
            return check_palindrome(start + 1, end - 1)
        else:
            return False
    
    # Call the recursive function starting from the beginning and end of the string
    return check_palindrome(start, end)