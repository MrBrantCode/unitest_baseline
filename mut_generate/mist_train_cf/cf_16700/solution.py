"""
QUESTION:
Create a function called `find_longest_palindrome` that takes a string as input and returns the longest palindrome within it that starts and ends with the same letter. The input string will not exceed 10^6 characters.
"""

def find_longest_palindrome(string):
    n = len(string)
    longest_palindrome = ""

    # Iterate through each character as the center of the palindrome
    for i in range(n):
        # Expand around the center to find palindromes
        palindrome = expand_around_center(string, i, i)  # Odd length palindrome
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

        if i < n-1:  # Ensure the right index doesn't exceed the string length
            palindrome = expand_around_center(string, i, i + 1)  # Even length palindrome
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

    return longest_palindrome

def expand_around_center(string, left, right):
    # Expand around the center characters to find palindromes
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    return string[left + 1: right]