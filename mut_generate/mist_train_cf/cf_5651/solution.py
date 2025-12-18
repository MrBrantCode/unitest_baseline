"""
QUESTION:
Implement a function `get_unique_strings(input_list)` that takes a list of strings as input, removes duplicates, and returns a new list with unique strings in the original order. The function should be able to handle large inputs (up to 1 million elements) efficiently.
"""

def entrance(input_list):
    unique_strings = []
    seen_strings = set()

    for string in input_list:
        if string not in seen_strings:
            seen_strings.add(string)
            unique_strings.append(string)

    return unique_strings