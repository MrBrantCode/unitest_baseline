"""
QUESTION:
Create a function `count_chars(s)` that calculates the frequency count of each unique alphanumeric character in a given string `s`. The function should return a dictionary where keys are the alphanumeric characters and values are their respective frequency counts. The function should be case-sensitive and count numeric and alphabetic characters separately.
"""

def count_chars(s):
    freq_dict = {}
    for char in s:
        if char.isalnum():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict