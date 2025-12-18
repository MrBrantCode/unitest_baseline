"""
QUESTION:
Write a function named `find_first_non_adjacent_repeating_element` that takes an array of integers as input and returns the first repeating element that is not adjacent to its previous occurrence. The output should be in the form of a dictionary with the repeating element as the key and its index as the value.
"""

def find_first_non_adjacent_repeating_element(arr):
    repeating_elements = {}
    for i in range(1, len(arr)):
        if arr[i] in repeating_elements and i - repeating_elements[arr[i]] > 1:
            return {arr[i]: i}
        elif arr[i] == arr[i - 1]:
            repeating_elements[arr[i]] = i
    return {}