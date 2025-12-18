"""
QUESTION:
Implement a function named `FunctionA` that takes an array of integers as input and returns a list of unique positive integers from the array in descending order.
"""

def FunctionA(arr):
    positive_set = set()
    for elem in arr:
        if elem > 0:
            positive_set.add(elem)
    return sorted(list(positive_set), reverse=True)