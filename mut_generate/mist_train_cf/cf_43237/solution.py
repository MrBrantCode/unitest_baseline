"""
QUESTION:
Write a function `longestPalindrome(s: str) -> str` to find the longest palindromic substring in a given string `s`, where a palindrome is a string that reads the same backward as forward. If there are multiple longest palindromic substrings, the function can return any one of them.
"""

def longestPalindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest