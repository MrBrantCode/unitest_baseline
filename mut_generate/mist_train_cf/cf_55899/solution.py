"""
QUESTION:
Write a function `parse_text(text)` that takes a string of key-value pairs as input, where pairs are separated by commas and nested pairs are separated by semicolons. The function should return an OrderedDict where keys are unique and the value of a repeated key is an aggregate of all occurrences, separated by commas.
"""

from collections import OrderedDict

def parse_text(text):
    od = OrderedDict()

    # split the text into chunks separated by semicolons
    chunks = text.split(';')

    # iterate over each chunk
    for chunk in chunks:

        # split the chunk into key-value pairs separated by commas
        pairs = chunk.split(',')

        # iterate over each pair
        for pair in pairs:
            
            # split the pair into key and value
            key, value = pair.split(':')

            # if the key already exists in the dictionary, append the new value to the existing value
            if key in od:
                od[key] += ',' + value
            else:
                od[key] = value

    return od