"""
QUESTION:
Create a function `remove_duplicates` that takes an array of positive integers as input, and returns a new array with all duplicates removed without modifying the original array. The function should have a time complexity of O(n), where n is the length of the input array, and should not use any built-in methods or data structures such as sets or dictionaries.
"""

def remove_duplicates(input_array):
    unique_elements = []
    seen_elements = set()

    for element in input_array:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)

    return unique_elements