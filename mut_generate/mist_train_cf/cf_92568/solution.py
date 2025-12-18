"""
QUESTION:
Create a function named `sort_values_by_length` that takes a dictionary as an input and returns the dictionary values in descending order of their lengths. In case of multiple values with the same length, maintain the original order.
"""

def sort_values_by_length(d):
    lengths = [(value, len(value)) for value in d.values()]
    sorted_lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
    sorted_values = [value for value, _ in sorted_lengths]
    return sorted_values