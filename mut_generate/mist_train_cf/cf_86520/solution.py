"""
QUESTION:
Implement a function `substring_check(haystack: str, needle: str) -> bool` that checks if a string `haystack` contains another string `needle` as a substring. The function should return `True` if the `haystack` string contains the `needle` string as a substring, and `False` otherwise. 

The function should satisfy the following constraints: 
- The time complexity should be O(n), where n is the length of the `haystack` string.
- The space complexity should be O(1).
"""

def substring_check(haystack: str, needle: str) -> bool:
    return needle in haystack