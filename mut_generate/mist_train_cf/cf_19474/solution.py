"""
QUESTION:
Design a function `reverse_string(string)` that reverses the characters of the input string in place without using any additional variables or data structures and without using the built-in 'reverse' method. The function should handle strings with special characters and whitespace correctly, and its time complexity should be O(n), where n is the length of the string.
"""

def reverse_string(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum() or s[left].isspace():
            left += 1
        elif not s[right].isalnum() or s[right].isspace():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    return ''.join(s)