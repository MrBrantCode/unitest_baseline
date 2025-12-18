"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string manipulation functions or libraries. Additionally, the function should not use any additional data structures such as lists, arrays, or stacks, and should only use basic operations such as indexing, swapping, and iteration.
"""

def entance(s):
    # Convert the string to a list of characters
    chars = list(s)
    
    # Initialize two pointers
    left = 0
    right = len(chars) - 1
    
    # Iterate until the pointers meet or cross each other
    while left < right:
        # Swap the characters at the left and right pointers
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string
    reversed_string = ''.join(chars)
    
    return reversed_string