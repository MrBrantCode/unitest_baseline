"""
QUESTION:
Create a function named `char_frequency` that takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding frequency occurrences. The function should consider each character in the string, including spaces and punctuation, as a distinct character.
"""

def char_frequency(statement):
    freq_dict = {}
    for i in statement:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict