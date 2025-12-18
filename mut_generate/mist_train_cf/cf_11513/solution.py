"""
QUESTION:
Create a function `sum_of_previous_and_next_elements` that takes a list of integers as input and returns a new list where each element is the sum of the previous and next elements in the original list. The first element should be treated as if it has a previous element of 0 and the last element as if it has a next element of 0. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def sum_of_previous_and_next_elements(lst):
    if len(lst) == 0:
        return []
    
    result = []
    for i in range(len(lst)):
        previous = lst[i-1] if i > 0 else 0
        next = lst[i+1] if i < len(lst)-1 else 0
        result.append(previous + next)
    
    return result