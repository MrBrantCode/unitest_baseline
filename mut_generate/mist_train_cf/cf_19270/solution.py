"""
QUESTION:
Write a function `remove_elements` that takes a list of integers as input and returns a new list with all elements that appear more than 10 times in the original list removed. The function should preserve the original order of elements in the list.
"""

def remove_elements(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    result = []
    for num in lst:
        if counts[num] <= 10:
            result.append(num)
    
    return result