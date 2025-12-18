"""
QUESTION:
A palindrome is a series of characters that read the same forwards as backwards such as "hannah", "racecar" and "lol".

For this Kata you need to write a function that takes a string of characters and returns the length, as an integer value, of longest alphanumeric palindrome that could be made by combining the characters in any order but using each character only once. The function should not be case sensitive.

For example if passed "Hannah" it should return 6 and if passed "aabbcc_yYx_" it should return 9 because one possible palindrome would be "abcyxycba".
"""

from collections import Counter

def longest_palindrome(s: str) -> int:
    # Convert the string to lowercase and filter out non-alphanumeric characters
    filtered_chars = filter(str.isalnum, s.lower())
    
    # Count the frequency of each alphanumeric character
    char_counts = Counter(filtered_chars)
    
    # Calculate the length of the longest palindrome
    palindrome_length = sum(v // 2 * 2 for v in char_counts.values())
    
    # Add one if there's any character with an odd count (which can be the center of the palindrome)
    if any(v % 2 for v in char_counts.values()):
        palindrome_length += 1
    
    return palindrome_length