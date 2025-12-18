"""
QUESTION:
Implement a function `reverse_string(s)` that takes a string `s` as input and returns its reverse without using any built-in string reversal functions or methods. The solution should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). Note that strings are immutable, so conversion to a mutable data structure may be necessary.
"""

def reverse_string(s):
    # Convert the string to a list since strings are immutable
    s = list(s)
    start = 0
    end = len(s) - 1
    
    # Iterate until start is less than end
    while start < end:
        # Swap characters at start and end
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    # Convert the list back to a string
    return ''.join(s)