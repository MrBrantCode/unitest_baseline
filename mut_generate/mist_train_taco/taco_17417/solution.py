"""
QUESTION:
Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace'].
"""

from itertools import accumulate

def accumulate_without_spaces(values):
    # Remove spaces from each string in the list
    values_without_spaces = [s.replace(' ', '') for s in values]
    # Accumulate the strings without spaces
    return list(accumulate(values_without_spaces))