"""
QUESTION:
Write a function `repeated_substring` that takes a string of length N as input and returns True if there is a substring in the string that repeats itself, and False otherwise. The function should consider all possible substrings of the input string.
"""

def repeated_substring(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            match = True
            for i in range(length, n, length):
                if s[:length] != s[i:i + length]:
                    match = False
                    break
            if match:
                return True
    return False