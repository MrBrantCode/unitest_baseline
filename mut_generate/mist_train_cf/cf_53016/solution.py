"""
QUESTION:
Create a function `least_frequent_char(input_string)` that takes a string `input_string` containing only alphanumerical characters and returns the character that appears with the least frequency. If multiple characters have the same least frequency, the function should return the first one it encounters. The function should be able to handle strings with a minimum length of 1.
"""

from collections import Counter

def least_frequent_char(input_string):
    counter = Counter(input_string)
    least_frequent_char = input_string[0]
    least_frequent_count = counter[input_string[0]]

    for char, count in counter.items():
        if count < least_frequent_count:
            least_frequent_char = char 
            least_frequent_count = count

    return least_frequent_char