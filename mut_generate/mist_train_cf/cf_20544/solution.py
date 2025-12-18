"""
QUESTION:
Create a function `sort_values_descending(d)` that takes a dictionary `d` as input and returns a list of its values in descending order of their lengths. If multiple values have the same length, maintain their original order.
"""

def sort_values_descending(d):
    # Create a list of tuples with lengths and keys
    length_key_list = [(len(value), key) for key, value in d.items()]

    # Sort the list in descending order based on the length
    length_key_list.sort(reverse=True)

    # Extract the values from the sorted list
    sorted_values = [d[key] for length, key in length_key_list]

    return sorted_values