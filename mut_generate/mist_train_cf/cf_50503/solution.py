"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers as input, removes duplicates, and returns the unique values in ascending order. Implement the function without using built-in functions like `set` or `sorted`, and without additional data structures like dictionaries or sets.
"""

def remove_duplicates(input_array):
    if not input_array:
        return []
    input_array = sorted(input_array)
    output_array = [input_array[0]]

    for i in range(1, len(input_array)):
        if input_array[i] != output_array[-1]:
            output_array.append(input_array[i])
    return output_array