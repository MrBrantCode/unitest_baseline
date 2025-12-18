"""
QUESTION:
Create a function `minOperations(s)` that takes a string `s` of up to 10^6 characters and returns the minimal number of operations (transformations) needed to make all characters within the string the same. The cost of transforming a character `c` to another character `target` is the absolute difference of their ASCII values. The function should be optimized to handle large strings efficiently.
"""

from collections import Counter

def minOperations(s: str) -> int:
    count = Counter(s) 
    target = max(count, key=count.get) 
    return sum(abs(ord(char) - ord(target)) for char in count)