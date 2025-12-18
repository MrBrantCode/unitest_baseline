"""
QUESTION:
Write a function named `solve` that takes an array of tuples as input. Each tuple can contain elements of different types like string, integer, and float. Sort the array of tuples in descending order based on the sum of numerical elements (integer and float) in each tuple, ignoring string and other types of elements.
"""

def solve(tuples):
    # Custom function to calculate the sum of numerical elements in a tuple
    def custom_sum(tuple):
        total = 0
        for i in tuple:
            if isinstance(i, (int, float)):
                total += i
        return total
    
    # Sort tuples based on the custom_sum function in descending order
    return sorted(tuples, key=custom_sum, reverse=True)