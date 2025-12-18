"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate integers removed while maintaining the original ascending order.
"""

def remove_duplicates(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result