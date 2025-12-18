"""
QUESTION:
Create a function named `freq_count` that calculates the frequency of each unique integer in a given list. The function should handle large lists efficiently, detect and return an error message for non-integer and null inputs, and provide a clear description of its memory management and computational complexity.
"""

def freq_count(lst):
    if lst is None:
        return "Input is null"
    freq_dict = {}
    for i in lst:
        if type(i) == int:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        else:
            return "Non-integer input detected."
    return freq_dict