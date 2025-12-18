"""
QUESTION:
Write a function `longest_palindrome(input_string)` that finds the longest palindromic substring in a given string. The function should handle both odd and even length palindromes and return the longest one.
"""

def longest_palindrome(input_string):
    def get_palindrome(input_string, i, j):
        while i >= 0 and j < len(input_string) and input_string[i] == input_string[j]:
            i -= 1
            j += 1
        return input_string[i + 1:j]

    longest = ''
    for k in range(len(input_string)):
        # odd len palindromes
        palindrome_odd = get_palindrome(input_string, k, k)
        if len(palindrome_odd) > len(longest): 
            longest = palindrome_odd
        # even len palindromes
        palindrome_even = get_palindrome(input_string, k, k + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest