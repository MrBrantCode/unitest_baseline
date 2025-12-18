"""
QUESTION:
Create a function named `char_frequency` that takes a string as an argument and returns a dictionary with each distinct character (excluding white spaces) as a key and its frequency in the string as a value. The function should treat capital and small letters as distinct characters.
"""

def char_frequency(str1):
    freq_dict = {}
    for n in str1:
        if n != ' ': 
            keys = freq_dict.keys()
            if n in keys:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1
    return freq_dict