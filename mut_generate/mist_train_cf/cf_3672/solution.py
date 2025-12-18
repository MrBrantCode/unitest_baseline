"""
QUESTION:
Write a function called `is_palindrome` that takes a string as input and returns a boolean value indicating whether or not the input string is a palindrome, ignoring non-alphanumeric characters and being case-insensitive. The function should not use any built-in functions or methods for string manipulation or comparison and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entrance(s):
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    
    # Continue checking characters while the pointers haven't crossed each other
    while left < right:
        # If the left character is not alphanumeric, move the left pointer to the right
        if not s[left].isalnum():
            left += 1
        # If the right character is not alphanumeric, move the right pointer to the left
        elif not s[right].isalnum():
            right -= 1
        # If the characters at the left and right pointers are different (ignoring case), return False
        elif s[left].lower() != s[right].lower():
            return False
        # If the characters at the left and right pointers are the same (ignoring case), move both pointers
        else:
            left += 1
            right -= 1
    
    # If the loop completes without returning False, the string is a palindrome
    return True