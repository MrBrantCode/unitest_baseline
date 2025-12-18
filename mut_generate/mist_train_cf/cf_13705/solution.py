"""
QUESTION:
Implement a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def reverse_string(s):
    start = 0
    end = len(s) - 1

    while start < end:
        # Swap characters at start and end positions
        temp = s[start]
        s = s[:start] + s[end] + s[start+1:]
        s = s[:end] + temp + s[end+1:]
        
        # Increment start and decrement end
        start += 1
        end -= 1

    return s