"""
QUESTION:
Write a function `find_palindrome_substring` that takes a set of strings and a minimum substring length as input and returns a set of unique palindromic substrings with a length greater than or equal to the specified minimum length that can be formed from the given strings. A palindromic substring must read the same backward as forward.
"""

def find_palindrome_substring(strings, substring_length):
    found_substrings = set()
    for string in strings:
        for i in range(len(string) - substring_length + 1):
            substring = string[i:i+substring_length]
            if substring == substring[::-1]:
                found_substrings.add(substring)
    return found_substrings