"""
QUESTION:
Write a recursive function named `nested_sum` that calculates the sum of all integers in a given list, including those in nested lists. The function should handle non-integer and non-list elements by printing an error message and ignoring them in the calculation.
"""

def nested_sum(nested_list):
    total = 0
    for elem in nested_list:
        if type(elem) == list:
            total += nested_sum(elem)
        else:
            try:
                total += elem
            except TypeError:
                print(f"Error: Invalid type {type(elem)} encountered. Only integers and lists are supported.")
    return total