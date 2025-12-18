"""
QUESTION:
Write a function `switch_string_order` that takes a string `str` as input, splits it at the midpoint, and returns a new string with the two parts in reverse order. If the length of the string is odd, the character at the midpoint should be included in the first part of the split. If the length of the string is even, the character at the midpoint should be included in the second part of the split.
"""

def switch_string_order(s):
    # Determine the midpoint index
    midpoint = len(s) // 2 + len(s) % 2 - 1
    
    # Split the string into two parts
    first_part = s[:midpoint + 1]
    second_part = s[midpoint + 1:]
    
    # Switch the order of the two parts
    return second_part + first_part