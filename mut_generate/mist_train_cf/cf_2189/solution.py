"""
QUESTION:
Create a function `reverse_string` that takes a string as input and returns the string in reverse order. The function must have a time complexity of O(n), where n is the length of the string, and it must only use a constant amount of extra space. The function should handle strings containing both printable ASCII characters and unicode characters properly. The input string can be empty.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    s = list(s)
    
    # Initialize the left and right pointers
    left = 0
    right = len(s) - 1
    
    # Swap characters until the pointers meet or cross each other
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string and return it
    return ''.join(s)