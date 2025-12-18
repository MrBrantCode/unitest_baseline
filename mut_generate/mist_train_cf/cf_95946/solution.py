"""
QUESTION:
Create a function named `generate_key_value_pair` that takes an array of mixed data types as input. The function should return a dictionary with a single key-value pair where the key is the sum of all integers in the array and the value is a list of even integers from the array, sorted in descending order. The function should ignore non-integer elements in the array.
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