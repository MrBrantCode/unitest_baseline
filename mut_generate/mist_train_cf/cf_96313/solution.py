"""
QUESTION:
Create a function `process_tuples(lst)` that takes a list of tuples as input. The function should filter out tuples with three or more elements where the sum of the first two elements is greater than 8, then sort the remaining tuples in descending order based on the first element of each tuple. The first element of each tuple should be a positive integer less than or equal to 10.
"""

def process_tuples(lst):
    result = []
    for tup in lst:
        if len(tup) >= 3 and sum(tup[:2]) > 8:
            continue
        result.append(tup)
    result.sort(key=lambda x: x[0], reverse=True)
    return result