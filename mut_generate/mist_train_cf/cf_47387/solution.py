"""
QUESTION:
Develop a function `longest_substring(string)` that returns a tuple containing the longest substring of `string` without repeating characters and its length. The function should be case sensitive.
"""

def longest_substring(s):
    start = maxLength = 0
    usedChar = {}

    for index, char in enumerate(s):
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char]+1
        else:
            maxLength = max(maxLength, index - start + 1)
        
        usedChar[char] = index

    return s[start:start+maxLength], maxLength