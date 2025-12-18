"""
QUESTION:
Create a function named 'char_frequency' that takes a string as input and returns a dictionary where the keys are the distinct characters in the string and the values are their corresponding frequencies.
"""

def char_frequency(str1):
    freq_dict = {}
    for n in str1:
        keys = freq_dict.keys()
        if n in keys:
            freq_dict[n] += 1
        else:
            freq_dict[n] = 1
    return freq_dict