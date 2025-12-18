"""
QUESTION:
Given a list of tuples where the first element of each tuple is a positive integer less than or equal to 10, write a function `process_tuples(lst)` that removes the third element if it exists and the sum of the first two elements is greater than 8, and then sorts the list in descending order based on the first element of each tuple.
"""

def process_tuples(lst):
    result = []
    for tup in lst:
        if len(tup) >= 3 and sum(tup[:2]) > 8:
            continue
        result.append(tup)
    result.sort(key=lambda x: x[0], reverse=True)
    return result