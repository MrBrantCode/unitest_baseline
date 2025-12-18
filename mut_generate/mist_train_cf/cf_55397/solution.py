"""
QUESTION:
Create a function `least_frequency` that takes an input string and returns the character that appears with the least frequency in the string along with its frequency count. The function should be able to handle any given string of characters. Note that if there are multiple characters with the same least frequency, any of them can be returned.
"""

def least_frequency(s):
    # Create a dictionary where the keys are characters and the values are their frequency.
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Find the least frequent character and its frequency.
    least_freq_char = min(freq_dict, key=freq_dict.get)
    least_freq_count = freq_dict[least_freq_char]
    return least_freq_char, least_freq_count