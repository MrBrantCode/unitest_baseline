"""
QUESTION:
Write a function `generate_key_value_pair(arr)` that takes an array of mixed elements as input and returns a dictionary with a single key-value pair. The key is the sum of all integer elements in the array, and the value is a list of all even integer elements in the array, sorted in descending order. The function should ignore non-integer elements in the array.
"""

def generate_key_value_pair(arr):
    sum_of_elements = 0
    even_numbers = []

    for element in arr:
        if isinstance(element, int):
            sum_of_elements += element
            if element % 2 == 0:
                even_numbers.append(element)

    even_numbers.sort(reverse=True)

    return {sum_of_elements: even_numbers}