"""
QUESTION:
Create a function `sort_string(s)` that takes a string `s` as input and returns a tuple containing the string sorted in alphabetical order and a dictionary with the frequency count of each character in the string. The function should handle spaces and case-sensitive characters, and the frequency count dictionary should be sorted.
"""

from collections import Counter

def sort_string(s):
    sorted_str_list = sorted(s)
    sorted_str = ''.join(sorted_str_list)
    freq_counter = dict(sorted(Counter(sorted_str_list).items()))
    return sorted_str, freq_counter