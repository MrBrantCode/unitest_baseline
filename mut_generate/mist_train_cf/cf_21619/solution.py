"""
QUESTION:
Write a recursive function `reverse_string` that takes a string `s` and an optional index `i` as input, reverses the string in-place without using any built-in string manipulation functions or data structures, and has a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_string(s, i=0):
    if i == len(s) // 2:  # Base case: reached the middle of the string
        return s
    
    # Swap the characters at indices i and len(s)-i-1
    s = s[:i] + s[len(s)-i-1] + s[i+1:len(s)-i-1] + s[i] + s[len(s)-i:]
    
    return reverse_string(s, i+1)