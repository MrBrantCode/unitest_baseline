"""
QUESTION:
Write a function `count_distinct_substrings(s)` that takes a string `s` of length `n` as input and returns the number of distinct continuous substrings in the string. The string can contain uppercase and lowercase letters, digits, and special characters. The function should have a time complexity of O(n^2) and a space complexity of O(n), where 1 ≤ n ≤ 10^6.
"""

def entance(s):
    n = len(s)
    substrings = set()

    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            substrings.add(substr)

    return len(substrings)