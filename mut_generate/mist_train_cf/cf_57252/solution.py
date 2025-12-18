"""
QUESTION:
Create a function named `char_frequency` that takes a string as input and returns a dictionary where the keys are unique characters in the string (regardless of case) and the values are their corresponding frequencies. The function should handle strings containing special characters and numerics.
"""

def char_frequency(s):
    s = s.lower()
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict