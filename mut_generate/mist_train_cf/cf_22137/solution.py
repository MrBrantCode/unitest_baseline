"""
QUESTION:
Write a function named `longest_vowel_string` that takes an array of lowercase strings as input. The function should find and return the longest string that starts with a vowel and has a length greater than 3. The input array will have at most 1000 elements.
"""

def longest_vowel_string(strings):
    longest = ""
    for string in strings:
        if string[0] in ['a', 'e', 'i', 'o', 'u'] and len(string) > len(longest) and len(string) > 3:
            longest = string
    return longest