"""
QUESTION:
Create a function `firstUniqueChar` that takes a string `s` as input and returns the index of the first unique character in the string. If the string contains all repetitive characters, the function should return -1. The function should handle strings with special characters, empty strings, and Unicode characters.

The function should satisfy the following conditions:
- If all characters in the string are repetitive, return -1.
- Consider special characters as normal characters.
- For an empty string, return -1.
- Correctly handle strings with Unicode characters.
"""

def firstUniqueChar(s: str) -> int:
    count = {}
    for i in range(len(s)):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
    
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
      
    return -1