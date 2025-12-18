"""
QUESTION:
Find all the multiples of a given base number within a specified range. Implement a function called `find_multiples` that takes three integers as parameters: the base number, the lower bound of the range, and the upper bound of the range. The function should return a list of all multiples of the base number that are greater than or equal to the lower bound and less than or equal to the upper bound.
"""

def find_multiples(base, lower, upper):
    output = []
    for i in range(lower, upper+1):
        if i % base == 0:
            output.append(i)
    return output