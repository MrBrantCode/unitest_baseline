"""
QUESTION:
Create a function named `sort_strings_by_length` that takes a list of strings and an integer `length_criteria` as input. The function should return a list of strings sorted by their absolute difference in length from the `length_criteria` and then alphabetically for strings with the same length difference.
"""

def sort_strings_by_length(lst, length_criteria):
    """Sort a list of strings based on the given length criteria"""
    return sorted(lst, key=lambda x: (abs(len(x) - length_criteria), x))