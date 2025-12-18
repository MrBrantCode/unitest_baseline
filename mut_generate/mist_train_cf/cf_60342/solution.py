"""
QUESTION:
Create a function `firstUniqChar` that finds the index position of the first unique character in a given string. The function should only use built-in functions or methods for determining the length of the string. The input string contains only letters and no special characters. If no unique character is found, return -1.
"""

def firstUniqChar(s: str) -> int:
    char_counts = {}
    for i in range(len(s)):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
            
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
            
    return -1