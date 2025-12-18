"""
QUESTION:
Create a function `extensive_sequence` that takes a list of strings and an integer `char_limit` as input, and returns the longest sequence of strings from the list where the total length of the strings does not exceed `char_limit`.
"""

def extensive_sequence(str_lst, char_limit):
    result = []
    aggregate_length = 0
    for s in str_lst:
        if aggregate_length + len(s) > char_limit:
            break
        aggregate_length += len(s)
        result.append(s)
    return result