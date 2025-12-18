"""
QUESTION:
Write a function `splitAndSwitch(s)` that takes a string `s` as input, splits it at the midpoint, and returns a new string with the two parts in reversed order. The midpoint should be rounded down to the nearest whole number if the string length is odd.
"""

def splitAndSwitch(s):
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return second_half + first_half