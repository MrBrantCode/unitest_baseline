"""
QUESTION:
Write a function named `count_substrings` that takes a string and an integer k as input, and returns the number of substrings with exactly k different characters. The function should return an error message if k is greater than the length of the string. The function should be case-insensitive and able to handle strings containing special characters, numbers, and uppercase letters.
"""

def count_substrings(s, k):
    if k > len(s):
        return "Error: k cannot be greater than the length of the string."
    
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            unique_chars = set(s[i:j].lower())
            
            if len(unique_chars) == k:
                count += 1
    
    return count