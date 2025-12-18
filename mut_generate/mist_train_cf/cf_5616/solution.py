"""
QUESTION:
Write a function `convert_list_to_dict` that takes a list of integers as input and returns a dictionary where each key is the sum of an even number and its index in the list, and its corresponding value is a list containing the index of the number in the original list, the square of the number, the cube of the number, and the factorial of the number. The function should include input validation to ensure the list only contains integers and is not empty, displaying an error message and terminating if the input is invalid.
"""

import math

def convert_list_to_dict(lst):
    if not all(isinstance(item, int) for item in lst) or not lst:
        print("Invalid input. List should only contain integers and should not be empty.")
        return

    result = {}
    for i, num in enumerate(lst):
        if num % 2 == 0:
            key = num + i
            value = [i, num ** 2, num ** 3, math.factorial(num)]
            result[key] = value

    return result