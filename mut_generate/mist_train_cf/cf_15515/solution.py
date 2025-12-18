"""
QUESTION:
Implement the `longest_palindromic_substring(s)` function that finds the longest palindromic substring in a given string `s` with a length not exceeding 1000 characters. The function should return the longest palindromic substring. The time complexity of the function should be less than O(n^2), where n is the length of the input string.
"""

def longest_palindromic_substring(s):
    t = '^#' + '#'.join(s) + '#$'
    n = len(t)
    P = [0] * n
    C = 0
    R = 0
    for i in range(1, n - 1):
        if i < R:
            P[i] = min(P[2 * C - i], R - i)
        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        if i + P[i] > R:
            R = i + P[i]
            C = i
    maxLenIndex = P.index(max(P))
    start = (maxLenIndex - P[maxLenIndex]) // 2
    end = start + P[maxLenIndex]
    return s[start:end]