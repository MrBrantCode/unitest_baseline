"""
QUESTION:
Implement a function `substring_check(haystack: str, needle: str) -> bool` that checks if a string `haystack` contains another string `needle` as a substring. The function should return `True` if the `haystack` string contains the `needle` string as a substring, and `False` otherwise. The function must satisfy the following constraints: 
- The time complexity should be O(n), where n is the length of the `haystack` string.
- The space complexity should be O(1).
Both the `haystack` and `needle` strings will only contain ASCII characters.
"""

def substring_check(haystack: str, needle: str) -> bool:
    haystack_len = len(haystack)
    needle_len = len(needle)
    
    if needle_len > haystack_len:
        return False
    
    for i in range(haystack_len - needle_len + 1):
        if haystack[i:i+needle_len] == needle:
            return True
    
    return False