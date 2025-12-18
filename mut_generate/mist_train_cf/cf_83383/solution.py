"""
QUESTION:
Write a function `solve_problem` that takes a list of numbers as input and returns the product of all numbers in the list that are congruent to 1 modulo 3.
"""

def solve_problem(numbers):
    product = 1
    for n in numbers:
        if n % 3 == 1:
            product *= n
    return product