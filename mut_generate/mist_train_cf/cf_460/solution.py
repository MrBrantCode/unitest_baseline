"""
QUESTION:
Implement a function `longest_palindrome(s)` that finds the longest palindromic substring in a given character sequence `s` with a length not exceeding 1000 characters. The function should have a time complexity less than O(n^2) and a space complexity less than O(n), where n is the length of the sequence, without using any built-in functions or libraries for string manipulation or palindrome detection.
"""

def longest_palindrome(s):
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i
        if right > i:
            p[i] = min(right - i, p[mirror])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    end = start + max_len
    return s[start:end]