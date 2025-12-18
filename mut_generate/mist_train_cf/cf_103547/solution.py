"""
QUESTION:
Create a function named `sort_values_by_length` that takes a dictionary as input and returns a list of its values in descending order of their lengths. If multiple values have the same length, maintain their original order.
"""

def sort_values_by_length(d):
    lengths = [(value, len(value)) for value in d.values()]
    sorted_lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
    sorted_values = [value for value, _ in sorted_lengths]
    return sorted_values