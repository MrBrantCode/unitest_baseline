"""
QUESTION:
Write a function named `sum_of_cubes` that calculates the sum of the cubes of the integers in a given list, rounds the sum to the nearest integer, and handles any exceptions that may occur during the calculation. The list may contain duplicate elements.
"""

def sum_of_cubes(arr):
    try:
        total = 0
        for num in arr:
            total += num ** 3
        return round(total)
    except:
        return "An error occurred while calculating the sum of cubes."