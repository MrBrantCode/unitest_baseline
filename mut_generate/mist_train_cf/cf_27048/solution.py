"""
QUESTION:
Implement a function `reverseStringWithNonAlphabetic` that takes a string `s` as input and returns the reverse of the string, while preserving the position of non-alphabetic characters. The function should return a string with all alphabetic characters reversed and non-alphabetic characters in their original positions.
"""

def reverseStringWithNonAlphabetic(s: str) -> str:
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    return ''.join(s)