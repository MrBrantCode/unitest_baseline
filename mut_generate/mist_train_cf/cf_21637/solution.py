"""
QUESTION:
Construct the Nth palindromic string with the given restrictions. 

Function name: construct_nth_palindrome

The function should take two parameters: a string and an integer N. It should return the Nth palindromic string, which must have at least 3 characters, contain at least one uppercase letter, one lowercase letter, and one special character, and not contain digits or whitespace characters.
"""

import string

def construct_nth_palindrome(input_string, N):
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