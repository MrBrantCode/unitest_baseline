"""
QUESTION:
Write a function `count_chars` that takes an array of strings as input and returns a dictionary where each key is a unique character from the input strings (case-insensitive) and each value is the total count of that character across all strings.
"""

def count_chars(arr):
    counter = {}
    for string in arr:
        for char in string.lower():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter