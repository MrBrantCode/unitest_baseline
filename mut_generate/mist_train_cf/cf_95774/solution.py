"""
QUESTION:
Design a function `is_palindrome` to check if a given string can be converted to a palindrome. The function should only consider alphanumeric characters and ignore case. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

def entrance(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True