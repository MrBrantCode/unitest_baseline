"""
QUESTION:
Write a function called `longestPalindrome` that finds the length of the longest palindrome substring in an input string. The function should have a time complexity of O(n^2) and a space complexity of O(1). The input string can contain upper and lowercase letters, numbers, and special characters. The function should consider all characters in the input string, including spaces and punctuation.
"""

def longestPalindrome(s):
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) < 2:
        return len(s)

    maxLength = 0

    for i in range(len(s)):
        length1 = expandAroundCenter(i, i)
        length2 = expandAroundCenter(i, i + 1)
        length = max(length1, length2)
        maxLength = max(maxLength, length)

    return maxLength