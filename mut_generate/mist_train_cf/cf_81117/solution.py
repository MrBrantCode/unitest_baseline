"""
QUESTION:
Write a function `length_of_longest_substring` that calculates the maximum length of a substring from a given string that does not contain any repeated characters. The function should take a string `s` as input and return the length of the longest substring without repeated characters. Assume that the input string only contains lowercase letters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def length_of_longest_substring(s):
    if not s:
        return 0
    
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength