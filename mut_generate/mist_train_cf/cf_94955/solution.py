"""
QUESTION:
Create a function `longest_palindrome_substring` that takes an input string and returns the length of the longest palindrome substring. The function should consider all characters in the input string, including spaces and punctuation, and should be able to handle upper and lowercase letters, numbers, and special characters.
"""

def longest_palindrome_substring(string):
    max_length = 0
    n = len(string)

    for i in range(n):
        # check for odd length palindromes
        left = i
        right = i
        while left >= 0 and right < n and string[left] == string[right]:
            length = right - left + 1
            if length > max_length:
                max_length = length
            left -= 1
            right += 1

        # check for even length palindromes
        left = i
        right = i + 1
        while left >= 0 and right < n and string[left] == string[right]:
            length = right - left + 1
            if length > max_length:
                max_length = length
            left -= 1
            right += 1

    return max_length