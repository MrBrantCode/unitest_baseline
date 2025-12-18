"""
QUESTION:
Design a function `longest_recurring_substring(s)` that identifies the longest recurring substring in a given string `s`, returning the substring along with its starting and ending index positions. If multiple substrings have the same maximum length, return all of them in the order they appear. The function should support strings of up to 10 million characters and handle potential issues like null or empty strings, memory overflow errors, and special characters.
"""

def longest_recurring_substring(s):
    n = len(s)
    LCSRe = [[0 for x in range(n + 1)] for y in range(n + 1)]
    res = ""
    res_length = 0
    index = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (s[i - 1] == s[j - 1] and LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
            else:
                LCSRe[i][j] = 0

    if (res_length > 0):
        for i in range(index - res_length + 1, index + 1):
            res = res + s[i - 1]

    return res