"""
QUESTION:
Write a function `longest_uppercase_run(s)` that takes a string `s` as input and returns the length of the longest run of consecutive uppercase letters in the string.
"""

def longest_uppercase_run(s):
    longest_run = 0
    current_run = 0
    
    for i in range(len(s)):
        if s[i].isupper():
            current_run += 1
        else:
            current_run = 0
        
        if current_run > longest_run:
            longest_run = current_run
    
    return longest_run