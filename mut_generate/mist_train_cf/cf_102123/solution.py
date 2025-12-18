"""
QUESTION:
Write a function named `isPalindrome` that takes a string `s` as input. The function should return `True` if the string is a palindrome (ignoring non-alphanumeric characters and considering the case) and `False` otherwise. The time complexity of the function should be O(n), where n is the length of the input string.
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