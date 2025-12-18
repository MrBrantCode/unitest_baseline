"""
QUESTION:
Reverse a string in-place without using any extra space or built-in functions, and maintain a time complexity of O(n), where n is the length of the input string. The function should be named `reverse_string` and take a string as an input. Note that since strings in the programming language are immutable, conversion to a mutable data structure may be necessary.
"""

def reversed_string(s):
    s = list(s)  # Convert string to a list
    left = 0  # Index of the first character
    right = len(s) - 1  # Index of the last character
    
    while left < right:
        # Swap the characters at the left and right indices
        s[left], s[right] = s[right], s[left]
        
        left += 1  # Increment left index
        right -= 1  # Decrement right index
        
    return ''.join(s)  # Convert the list back to a string