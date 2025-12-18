"""
QUESTION:
Write a function named `longest_substring` that takes a string as input and returns the longest substring of consecutive characters that contains at least one vowel. If multiple substrings have the same maximum length, return the first occurrence. The string only contains lowercase English letters.
"""

def longest_substring(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    longest = ''
    current = ''
    
    for char in s:
        if char in vowels:
            current += char
            if len(current) > len(longest):
                longest = current
        else:
            current = ''
    
    return longest