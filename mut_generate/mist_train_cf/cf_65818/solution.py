"""
QUESTION:
Write a function `zigzag_merge(s1, s2)` that merges two input strings `s1` and `s2` into a single string in a zigzag pattern. The function should iterate through both strings, adding characters from each string in an alternating manner. If the lengths of the strings are unequal, append the remaining characters of the longer string at the end of the resultant string. The solution should achieve a time complexity of O(n), where n is the length of the longer input string.
"""

def zigzag_merge(s1, s2):
    result = ''
    len1 = len(s1)
    len2 = len(s2)
    i = 0
    j = 0

    while i < len1 or j < len2:
        if i < len1:
            result += s1[i]
            i += 1

        if j < len2:
            result += s2[j]
            j += 1

    return result