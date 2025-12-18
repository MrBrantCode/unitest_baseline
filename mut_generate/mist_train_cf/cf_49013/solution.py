"""
QUESTION:
Given a string of lowercase English alphabets, write a function `print_operations(s)` to determine the minimum number of operations a unique printing apparatus needs to execute to replicate the string accurately. The printer can print a continuous series of identical characters in a single operation and can commence and terminate printing at any given point, superseding any characters that were previously printed. The length of the input string will not exceed 100 characters.
"""

def print_operations(s):
    operations = 1 if s else 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            operations += 1
    return operations