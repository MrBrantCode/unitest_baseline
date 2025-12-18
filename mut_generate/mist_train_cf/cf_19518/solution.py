"""
QUESTION:
Create a function named `sum_of_cubes` that takes a list of integers as input, calculates the sum of the cubes of the list elements, and returns the sum rounded to the nearest integer. The function should handle any exceptions that may occur during the calculation.
"""

def sum_of_cubes(arr):
    try:
        total = 0
        for num in arr:
            total += num ** 3
        return round(total)
    except:
        return "An error occurred while calculating the sum of cubes."