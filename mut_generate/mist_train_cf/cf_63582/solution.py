"""
QUESTION:
Write a function `median(l)` that calculates the median of a list of integers without sorting the original list. The function should work for both even and odd length lists and return the median as a float.
"""

def entrance(l: list):
    n = len(l)
    s = sorted(l)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)