"""
QUESTION:
Write a Python function `digit_count(s)` that takes a string `s` as input and returns a tuple containing the total count of digits in the string and a dictionary where the keys are the digits (0-9) and the values are their corresponding frequencies.
"""

def digit_count(s):
    count = 0
    freq = {str(x): 0 for x in range(10)}
    for char in s:
        if char.isdigit():
            count += 1
            freq[char] += 1
    return count, freq