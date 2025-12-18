"""
QUESTION:
Create a function named `find_longest_palindrome` that takes a non-empty string as input, removes spaces and punctuation marks, and returns the first occurrence of the longest palindrome in the string. The palindrome check should be case-insensitive.
"""

def find_longest_palindrome(s):
    s = ''.join(e for e in s if e.isalnum())
    
    longest_palindrome = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
                
    return longest_palindrome