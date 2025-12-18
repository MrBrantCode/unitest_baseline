"""
QUESTION:
Write a function `filter_unique_strings` that takes a list of strings as input, filters out the unique strings, and returns them in descending order based on their lengths. The input list can contain up to 10^6 strings, each with a maximum length of 100 characters, and the function should have a time complexity of O(nlogn) or better, where n is the length of the input list.
"""

from collections import Counter

def filter_unique_strings(strings):
    # Count the frequency of each string
    freq_counter = Counter(strings)
    
    # Filter out strings with frequency 1
    unique_strings = [string for string, freq in freq_counter.items() if freq == 1]
    
    # Sort the unique strings in descending order based on their lengths
    unique_strings.sort(key=lambda string: len(string), reverse=True)
    
    return unique_strings