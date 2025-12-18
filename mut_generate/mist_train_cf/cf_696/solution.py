"""
QUESTION:
Create a function called `combine_strings` that takes two strings as parameters and returns a new string where each character from the first string is followed by its corresponding character from the second string, ignoring non-alphabetic characters and handling case-insensitive matching. If the two strings are not of equal length, the remaining characters from the longer string should be appended to the end of the concatenated string. The function should also remove any duplicate characters from the concatenated string and have a time complexity of O(n) and a space complexity of O(n), where n is the length of the longer string after removing non-alphabetic characters.
"""

def combine_strings(str1, str2):
    str1 = ''.join([c.lower() for c in str1 if c.isalpha()])
    str2 = ''.join([c.lower() for c in str2 if c.isalpha()])
    combined = ''
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        combined += str1[i] + str2[j]
        i += 1
        j += 1
    if i < len(str1):
        combined += str1[i:]
    if j < len(str2):
        combined += str2[j:]
    return ''.join(sorted(set(combined), key=combined.index))