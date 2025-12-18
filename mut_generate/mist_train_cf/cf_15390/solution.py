"""
QUESTION:
Create a function called `sort_strings_by_length` that takes a list of strings as input. The function should return a list of strings sorted by their length in descending order, excluding strings with lengths less than or equal to 3. The function should not use the built-in sort method.
"""

def sort_strings_by_length(strings):
    string_lengths = {}
    for string in strings:
        if len(string) > 3:
            string_lengths[len(string)] = string

    sorted_lengths = sorted(string_lengths.keys(), reverse=True)
    result = []
    for length in sorted_lengths:
        result.append(string_lengths[length])

    return result