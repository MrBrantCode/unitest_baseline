"""
QUESTION:
Write a function `avg_of_list(lst)` that calculates the average of all numeric elements in a given list, skipping non-numeric elements. The function should return the average as a float if there are numeric elements, and None if the list contains no numeric elements.
"""

def avg_of_list(lst):
    total = 0
    count = 0
    for i in lst:
        if isinstance(i, (int, float)):
            total += i
            count += 1
    if count == 0:
        return None  
    else:
        return total/count