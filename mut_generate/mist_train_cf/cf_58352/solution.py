"""
QUESTION:
Write a function named `count_unique_chars` that takes an array of strings as input and returns the number of unique characters in the array. The input array will contain 10 strings, each consisting of 10 random lowercase English letters. The function should ignore duplicate characters and only count each unique character once.
"""

def count_unique_chars(arr):
    return len(set(''.join(arr)))