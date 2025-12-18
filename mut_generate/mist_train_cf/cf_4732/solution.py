"""
QUESTION:
Create a function `calculate_sum_of_cubes(arr)` that calculates the sum of the cubes of the elements in the input array. The function should only accept arrays with 5-10 elements, containing unique positive integers in the range 1-100. The sum of the cubes must be divisible by both 3 and 5, and must not exceed 10000. The function should return the sum of the cubes as a float rounded to two decimal places. If any of these conditions are not met, the function should return an error message. The function should also handle invalid input types (e.g. strings, booleans) and return an error message.
"""

def entrance(arr):
    # Check if array length is valid
    if len(arr) < 5 or len(arr) > 10:
        return "Error: Array length must be between 5 and 10."

    # Check if array contains only positive integers in the range of 1 to 100
    if not all(isinstance(x, int) and 1 <= x <= 100 for x in arr):
        return "Error: Array must only contain positive integers in the range of 1 to 100."

    # Check if array contains duplicate elements
    if len(arr) != len(set(arr)):
        return "Error: Array contains duplicate elements."

    # Calculate the sum of the cubes
    sum_of_cubes = sum(x ** 3 for x in arr)

    # Check if the sum is divisible by 3 and 5
    if sum_of_cubes % 3 != 0 or sum_of_cubes % 5 != 0:
        return "Error: The sum of the cubes is not divisible by 3 and 5."

    # Check if the sum exceeds 10000
    if sum_of_cubes > 10000:
        return "Error: The sum of the cubes exceeds 10000."

    return round(sum_of_cubes, 2)