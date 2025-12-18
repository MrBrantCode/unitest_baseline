"""
QUESTION:
Write a function `increase_and_multiply(tuples)` that takes a list of tuples as input and returns a new list with the value of each tuple increased by one if the sum of the tuple's values is even, or multiplied by two if the sum is odd.
"""

def increase_and_multiply(tuples):
    result = []
    for tup in tuples:
        value_sum = sum(tup)
        if value_sum % 2 == 0:
            result.append((tup[0]+1, tup[1]+1))
        else:
            result.append((tup[0]*2, tup[1]*2))
    return result