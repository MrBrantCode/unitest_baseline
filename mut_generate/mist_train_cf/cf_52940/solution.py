"""
QUESTION:
Write a function called `median` that takes a list of numbers as input and returns its median without modifying the original list. The function should work for lists with both even and odd number of elements.
"""

def median(lst: list):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n%2] if n else None