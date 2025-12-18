"""
QUESTION:
Write a function `product(arr)` that takes an array of numbers as input and returns the product of the elements within the array. The function should handle potential exceptions or errors that may arise when dealing with input from users, such as non-list inputs or lists containing non-numeric elements.
"""

def product(arr):
    try:
        total_product = 1
        for i in arr:
            total_product *= i
        return total_product
    except TypeError:
        print("Error: The input is not a valid list of numbers. Please enter a valid list of numbers.")