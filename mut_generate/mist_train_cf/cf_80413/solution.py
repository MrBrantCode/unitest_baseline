"""
QUESTION:
Create a function called `are_anagrams_and_palindromes(str1, str2)` that takes two input strings and returns True if both strings are anagrams of each other and palindromes, and False otherwise. The function should be case sensitive and ignore special characters or spaces. The input strings `str1` and `str2` will only contain alphanumeric characters, spaces, and special characters.
"""

def are_anagrams_and_palindromes(str1, str2):
    def clean_input(input_str):
        return ''.join(e for e in input_str if e.isalnum()).lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    def is_palindrome(input_str):
        return input_str == input_str[::-1]

    str1 = clean_input(str1)
    str2 = clean_input(str2)

    return is_anagram(str1, str2) and is_palindrome(str1) and is_palindrome(str2)