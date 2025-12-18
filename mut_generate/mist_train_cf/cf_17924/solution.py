"""
QUESTION:
Create a function named `longest_palindrome_substring` that takes one string argument. This function should return the length of the longest palindrome substring within the given string, considering all characters including spaces and punctuation.
"""

def longest_palindrome_substring(string):
    max_length = 0
    start = 0
    n = len(string)

    for i in range(n):
        # check for odd length palindromes
        left = i
        right = i
        while left >= 0 and right < n and string[left] == string[right]:
            length = right - left + 1
            if length > max_length:
                max_length = length
                start = left
            left -= 1
            right += 1

        # check for even length palindromes
        left = i
        right = i + 1
        while left >= 0 and right < n and string[left] == string[right]:
            length = right - left + 1
            if length > max_length:
                max_length = length
                start = left
            left -= 1
            right += 1

    return max_length