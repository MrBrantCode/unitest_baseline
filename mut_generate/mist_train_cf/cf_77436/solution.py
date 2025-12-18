"""
QUESTION:
Create a function called `frequency_counter` that accepts a list of strings. The function should return a dictionary where each key is a string from the input list, and its corresponding value is another dictionary containing two keys: "Frequency" and "Max". The "Frequency" key maps to a dictionary with characters from the string as keys and their frequencies as values, sorted in descending order by frequency and then in ascending lexicographic order. The "Max" key maps to the character with the highest frequency; in case of a tie, the character that comes first alphabetically should be chosen.
"""

import collections

def frequency_counter(strings):
    output = {}
    for string in strings:
        frequency_dict = collections.Counter(string)
        frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: (-item[1], item[0])))  
        max_value = max(list(frequency_dict.values()))
        max_keys = [k for k, v in frequency_dict.items() if v == max_value]
        output[string] = {"Frequency": frequency_dict, "Max": max_keys[0]}  
    return output