"""
QUESTION:
Write a function called `lengthOfMaxPalindrome` that takes a string `s` and an integer `n` as parameters. The function should check all substrings of `s` that start at index `n` to find the longest palindromic substring. If multiple palindromic substrings have the same maximum length, return the length of the first one encountered. If no palindromic substring exists from index `n`, return "No Palindrome". A single character is considered a palindrome.
"""

def lengthOfMaxPalindrome(s, n):
    def isPalindrome(temp_str):
        i = 0
        j = -1
        while i < len(temp_str) // 2:
            if temp_str[i] != temp_str[j]:
                return False
            i += 1
            j -= 1
        return True

    max_length = 0
    for i in range(n, len(s)):
        for j in range(n, i + 1):
            temp_str = s[j:i+1]
            if isPalindrome(temp_str):
                if len(temp_str) > max_length:
                    max_length = len(temp_str)

    return max_length if max_length else "No Palindrome"