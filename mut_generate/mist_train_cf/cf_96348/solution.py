"""
QUESTION:
Create a function `sort_string_lengths` that takes an array of strings, removes duplicates, and returns a dictionary with the unique strings as keys and their lengths as values, sorted in ascending order of the lengths.
"""

def sort_string_lengths(arr):
    unique_strings = list(set(arr))  # Remove duplicates from the input array
    string_lengths = {string: len(string) for string in unique_strings}  # Create a dictionary with string lengths as values
    sorted_lengths = sorted(string_lengths.items(), key=lambda x: x[1])  # Sort the dictionary by values in ascending order
    sorted_dict = dict(sorted_lengths)  # Convert the sorted list of tuples back into a dictionary
    return sorted_dict