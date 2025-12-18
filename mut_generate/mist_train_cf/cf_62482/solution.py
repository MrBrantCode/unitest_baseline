"""
QUESTION:
Create a function named `count_palindrome` that takes an input string and the length of the substring as parameters. The function should count and return the number of palindromic substrings of the given length in the input string. 

A palindromic substring is a substring that reads the same backward as forward. The function should consider overlapping substrings as separate, and the length of the substring should be at least 2.
"""

def count_palindrome(input_str, length):
    count = 0
    for i in range(len(input_str) - length + 1):
        if input_str[i:i+length] == input_str[i:i+length][::-1]:
            count += 1
    return count