"""
QUESTION:
Write a Python function `construct_nth_palindrome(N)` to construct the Nth palindromic string. The palindromic string should have at least 3 characters and must contain at least one uppercase letter, one lowercase letter, and one special character (not a digit or a whitespace character). The function should return an empty string if N is less than 1.
"""

import string

def construct_nth_palindrome(N):
    if N < 1:
        return ""

    result = ""
    count = 0

    for upper in string.ascii_uppercase:
        for lower in string.ascii_lowercase:
            for special in string.punctuation:
                palindrome = special + lower + upper + lower + special
                if any(char.isupper() for char in palindrome) and \
                   any(char.islower() for char in palindrome) and \
                   any(char in string.punctuation for char in palindrome) and \
                   not any(char.isdigit() for char in palindrome) and \
                   not any(char.isspace() for char in palindrome):
                    count += 1
                    if count == N:
                        result = palindrome
                        break
            if count == N:
                break
        if count == N:
            break

    return result