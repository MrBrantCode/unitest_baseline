"""
QUESTION:
Write a function called `increase_and_multiply` that takes a list of tuples as input. The function should return a new list of tuples where each tuple's values are increased by one if the sum of the original tuple's values is even, otherwise each value should be multiplied by two.
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