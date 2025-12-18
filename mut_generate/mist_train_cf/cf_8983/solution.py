"""
QUESTION:
Write a function `remove_duplicates` that takes a string of ASCII characters as input and returns a string with all duplicate characters removed. The input string has a maximum length of 10^6 characters. The function must have a time complexity of O(n), where n is the length of the input string, and must not use any additional data structures beyond a fixed amount of extra memory.
"""

def remove_duplicates(s):
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    seen = set()
    result = []
    
    for idx, char in enumerate(s):
        if char not in seen and idx == last_occurrence[char]:
            result.append(char)
            seen.add(char)
    
    return ''.join(result)