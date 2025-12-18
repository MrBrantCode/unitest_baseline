"""
QUESTION:
Find the longest string that starts with a vowel ('a', 'e', 'i', 'o', 'u') and has a length greater than 3 in an array of lowercase strings. The function should be named `longest_vowel_string` and it should take an array of strings as input. The array will have at most 1000 elements.
"""

def longest_vowel_string(strings):
    longest = ""
    for string in strings:
        if string[0] in ['a', 'e', 'i', 'o', 'u'] and len(string) > len(longest):
            longest = string
    return longest