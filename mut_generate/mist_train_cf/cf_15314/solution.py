"""
QUESTION:
Write a function called `longest_palindrome` that finds the longest palindrome in a given string. The function should ignore any whitespace or special characters and only consider palindromes with at least 5 characters. The solution should not use any built-in functions or libraries for string manipulation, except for the `len()` function, and should have a time complexity of O(n^2) or better.
"""

def longest_palindrome(s):
    max_len = 0
    max_palindrome = ""
    s = "".join(s.split())  # remove whitespace
    s = "".join(filter(str.isalnum, s))  # remove special characters
    n = len(s)
    def is_palindrome(substring):
        i, j = 0, len(substring) - 1
        while i < j:
            if substring[i] != substring[j]:
                return False
            i += 1
            j -= 1
        return True

    for i in range(n):
        for j in range(i + 4, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > max_len:
                max_len = len(substring)
                max_palindrome = substring
    return max_palindrome