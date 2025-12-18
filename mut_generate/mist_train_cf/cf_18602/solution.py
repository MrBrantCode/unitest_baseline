"""
QUESTION:
Write a function called `calculate_square` and `fill_dictionary` to fill a dictionary with keys as numbers and values as strings representing the square of the corresponding key. The dictionary should be filled from 1 to a specified number. The `calculate_square` function should use a recursive approach to calculate the square, handling negative numbers by converting them into positive numbers before performing the calculation. The `fill_dictionary` function should handle cases where the specified number is not a positive integer by printing an error message and returning an empty dictionary.
"""

def calculate_square(n):
    if n == 0:
        return 0
    elif n < 0:
        return calculate_square(-n)
    else:
        return calculate_square(n-1) + 2*n - 1

def fill_dictionary(num):
    if num < 1:
        print("Please enter a positive integer.")
        return {}
    
    dictionary = {}
    for i in range(1, num+1):
        dictionary[i] = str(calculate_square(i))
    
    return dictionary