"""
QUESTION:
Write a function called `char_frequency` that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the frequency of the characters in the string. The function should ignore non-alphabetical characters, treat both uppercase and lowercase letters as case-insensitive, and sort the keys in descending order based on their frequencies. In case two characters have the same frequency, they should be sorted lexicographically (in ascending order). The function should have a time complexity of O(n) or better, where n is the length of the input string.
"""

from collections import Counter

def char_frequency(input_string):
    # filter out non-alphabetical characters and unify case
    filtered_string = ''.join(ch for ch in input_string if ch.isalpha()).lower()

    # count the frequency of each character
    frequency_counter = Counter(filtered_string)

    # sort by frequency (descending) then alphabetically (ascending)
    sorted_frequency_counter = dict(sorted(frequency_counter.items(), key=lambda x: (-x[1], x[0])))

    return sorted_frequency_counter