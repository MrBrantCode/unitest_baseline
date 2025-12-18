"""
QUESTION:
Create a function `longest_palindrome(s)` that takes a string `s` as input and returns the longest palindrome substring. The function should handle strings with both uppercase and lowercase letters, special characters, and spaces, and ignore non-alphanumeric characters when checking for palindromes.
"""

def longest_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    longest_palindrome = ''
    max_length = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > max_length:
                    longest_palindrome = substring
                    max_length = len(substring)
    return longest_palindrome