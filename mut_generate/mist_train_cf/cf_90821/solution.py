"""
QUESTION:
Design a function called `sum_of_squares_of_evens` that takes a list of integers as input and returns the sum of the squares of all the even numbers in the list.
"""

def sum_of_squares_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:  
            total += num ** 2  
    return total