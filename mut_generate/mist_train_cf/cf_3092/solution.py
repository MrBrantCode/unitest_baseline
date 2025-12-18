"""
QUESTION:
Create a function called `longestPalindrome` that finds the length of the longest palindrome substring in an input string. The function should consider all characters in the input string, including spaces and punctuation. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longestPalindrome(s):
    if len(s) < 2:
        return len(s)

    start = 0
    maxLength = 0

    for i in range(len(s)):
        length1 = expandAroundCenter(s, i, i)
        length2 = expandAroundCenter(s, i, i + 1)
        length = max(length1, length2)
        if length > maxLength:
            maxLength = length
            start = i - (length - 1) // 2

    return maxLength