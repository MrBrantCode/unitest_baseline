"""
QUESTION:
Implement a function `find_longest_palindrome` that takes a string `s` as input and returns the longest palindrome within `s` that starts and ends with the same letter. The length of `s` will not exceed 10^6 characters.
"""

def entrance(s):
    n = len(s)
    longest_palindrome = ""

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    for i in range(n):
        palindrome = expand_around_center(i, i)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

        if i < n - 1:
            palindrome = expand_around_center(i, i + 1)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

    return longest_palindrome