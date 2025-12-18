"""
QUESTION:
Write a function named `longest_uppercase_run` that takes a string `s` as input and returns the length of the longest run of consecutive uppercase letters in the string. The function should iterate through the string to find the longest sequence of uppercase letters and return its length. The function should return 0 if the input string is empty.
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