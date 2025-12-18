"""
QUESTION:
Write a function `findShortestPalindrome` that takes a string as input and returns the shortest possible palindrome that can be created by appending characters to the end of the string. The function should use the KMP algorithm to find the longest proper prefix that is also a proper suffix of the string.
"""

def findShortestPalindrome(s):
    reversed_s = s[::-1]
    new_s = s + '#' + reversed_s
    lps = [0] * len(new_s)
    i, j = 1, 0
    while i < len(new_s):
        if new_s[i] == new_s[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return s + reversed_s[lps[-1]:]