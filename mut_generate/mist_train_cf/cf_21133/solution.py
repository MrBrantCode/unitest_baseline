"""
QUESTION:
Implement a function named `is_palindrome` that checks if a given input string is a palindrome. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1). The solution should not use any built-in functions or libraries that directly solve the problem. The function should return True if the input string is a palindrome and False otherwise.
"""

def is_palindrome(s):
    # Convert the input string to lowercase
    s = s.lower()
    
    # Initialize two pointers, one at the start and one at the end of the string
    start = 0
    end = len(s) - 1
    
    # Iterate until the two pointers meet or cross each other
    while start < end:
        # If the characters at the two pointers are not equal, return False
        if s[start] != s[end]:
            return False
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # If the loop completes without returning False, the string is a palindrome
    return True