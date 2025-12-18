"""
QUESTION:
Create a function `char_freq` that takes two lists as input: a list of strings and a list of integers representing positional indices. The function should evaluate characters at the given indices in the strings, ignoring strings that are shorter than the index. It should return a dictionary containing the frequency of each distinct character across all evaluated string positions.
"""

def char_freq(list_of_strings, list_of_indices):
    freq_dict = {}  # Initialize the empty dictionary
    for string in list_of_strings:
        for index in list_of_indices:
            if index < len(string):  # Ignore if string is shorter than the index
                char = string[index]  # Get the character at index position
                if char in freq_dict:  # If char already in dictionary, increment its count
                    freq_dict[char] = freq_dict.get(char) + 1
                else:  # If char not in dictionary, add it
                    freq_dict[char] = 1
    return freq_dict