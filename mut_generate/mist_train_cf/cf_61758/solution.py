"""
QUESTION:
Write a function `compute_aggregate` that takes an array as input and returns the sum of all numeric elements, including numeric strings and numbers within nested arrays. Non-numeric strings should be ignored.
"""

def compute_aggregate(arr):
    aggregate = 0
    for item in arr:
        if type(item) == list:
            aggregate += compute_aggregate(item)
        elif type(item) == str:
            if item.isdigit():
                aggregate += int(item)
        elif type(item) == int or type(item) == float:
            aggregate += item
    return aggregate