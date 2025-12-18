"""
QUESTION:
Implement a function named `reverse_string` that takes a string `s` as input and returns the reverse of the string using only iterative techniques, without using any built-in functions or methods that directly reverse a string or recursion.
"""

def reverse_string(s):
    # Convert the string into a list of characters
    chars = list(s)
    
    # Initialize two pointers at the start and end of the list
    left = 0
    right = len(chars) - 1
    
    # Swap characters at the pointers and move them towards the center
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Join the reversed characters and return the result
    reversed_string = ''.join(chars)
    return reversed_string