"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the input string, and use only constant extra space. It should not create any new strings or data structures other than the input string and a few variables.
"""

def reverse_string(s):
    if s == "":
        return s
    
    s = list(s)  # Convert string to list to allow in-place swapping
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters at left and right indices
        left += 1
        right -= 1
    
    return "".join(s)  # Convert list back to string