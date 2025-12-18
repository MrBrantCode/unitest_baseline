"""
QUESTION:
Create a function named `find_longest_palindrome` that takes a non-empty string as input and returns the first occurrence of the longest palindrome in the string. The palindrome should be case-insensitive, and the function should handle strings with spaces and punctuation marks by ignoring them.
"""

def find_longest_palindrome(string):
    # Remove spaces and punctuation marks from the string
    string = ''.join(e for e in string if e.isalnum())
    
    # Find the longest palindrome in the string
    longest_palindrome = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    
    return longest_palindrome