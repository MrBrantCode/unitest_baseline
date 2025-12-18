"""
QUESTION:
Write a function named `get_average()` that takes a list as input, calculates the average of all integers and floats in the list, and ignores any strings, lists, and dictionaries. The function should handle nested lists and dictionaries and have a time complexity of O(n), where n is the total number of elements in the list. Do not use built-in functions or libraries that directly solve this problem.
"""

def get_average(lst):
    total = 0
    count = 0
    
    for item in lst:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        elif isinstance(item, list):
            sub_total, sub_count = get_average(item)
            total += sub_total
            count += sub_count
        elif isinstance(item, dict):
            sub_total, sub_count = get_average(list(item.values()))
            total += sub_total
            count += sub_count
    
    if count == 0:
        return 0, 0
    
    return total, count

def entrance(lst):
    total, count = get_average(lst)
    if count == 0:
        return 0
    return total / count