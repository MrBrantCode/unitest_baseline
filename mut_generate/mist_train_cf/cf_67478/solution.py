"""
QUESTION:
Write a function named `sort_mixed_list` that sorts a given list of strings in ascending order based on the numeric value embedded in each string. The function should extract the numeric part from each string and use it as the key for sorting. The list contains strings that start with an alphabetic character followed by one or more digits.
"""

def sort_mixed_list(mix_list):
    # extract numeric part from string and convert it to int
    def numeric_value(item):
        value = ''.join(filter(str.isdigit, item))
        return int(value)

    # sort list using numeric values
    mix_list.sort(key=numeric_value)

    return mix_list