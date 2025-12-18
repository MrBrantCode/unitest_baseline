"""
QUESTION:
Write a function called `isPalindrome(s)` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome, ignoring any non-alphanumeric characters and considering the case of characters. The function should achieve a time complexity of O(n), where n is the length of the input string.
"""

def isPalindrome(s):
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the next alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare the characters at the two pointers
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    return True