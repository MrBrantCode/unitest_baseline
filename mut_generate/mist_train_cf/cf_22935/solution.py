"""
QUESTION:
Write a function `longest_palindromic_substring` that finds the longest palindromic substring of a given input string `s`. The function should have a time complexity of O(n) and use a constant amount of additional memory. The input string `s` can contain any characters, including special characters and spaces, and has a length of at most 10^5. The function should not use any string manipulation functions or methods.
"""

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s

    t = '#' + '#'.join(s) + '#'
    p = [0] * len(t)
    center = 0
    right = 0

    for i in range(len(t)):
        if center - right < i:
            mirror = 2 * center - i
            if mirror >= 0 and i < right:
                p[i] = min(right - i, p[mirror])

        while i - p[i] - 1 >= 0 and i + p[i] + 1 < len(t) and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_value = max(p)
    index = p.index(max_value)
    start = (index - max_value + 1) // 2

    longest_palindrome = s[start: start + max_value]
    return longest_palindrome