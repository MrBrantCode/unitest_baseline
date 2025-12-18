"""
QUESTION:
Create a function named `sum_of_cubes` that calculates the sum of the cubes of the elements in an array. The array must contain at least 5 elements and only positive integers. The function should return the sum of the cubes as a float rounded to two decimal places if the sum is divisible by 3; otherwise, it should return an error message.
"""

def sum_of_cubes(arr):
    if len(arr) < 5:
        return "Error: The array must contain at least 5 elements."

    for num in arr:
        if num <= 0 or type(num) != int:
            return "Error: The array must contain only positive integers."
    
    sum_cubes = 0
    for num in arr:
        sum_cubes += num ** 3

    if sum_cubes % 3 != 0:
        return "Error: The sum of the cubes is not divisible by 3."

    return round(sum_cubes, 2)