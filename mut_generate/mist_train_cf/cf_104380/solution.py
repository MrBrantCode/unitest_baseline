"""
QUESTION:
Write a function called `get_unique_cubes` that takes a list of unique positive integers as input, removes any duplicates, and returns a list of cubes of the unique numbers in the input list. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

def entrance(numbers):
    unique_numbers = list(set(numbers))
    cubes = [num**3 for num in unique_numbers]
    return cubes