"""
QUESTION:
Write a function called `unique_max` that takes a list of numbers and an optional boolean argument `find_max` (defaulting to `True`) as input. The function should return the index of the maximum number in the list if `find_max` is `True`, or the index of the minimum number if `find_max` is `False`, but only if the respective number is singularly unique in the list; otherwise, return -1.
"""

def unique_max(numbers, find_max=True):
    if find_max:
        max_num = max(numbers)
        if numbers.count(max_num) == 1:
            return numbers.index(max_num)
        else:
            return -1
    else:
        min_num = min(numbers)
        if numbers.count(min_num) == 1:
            return numbers.index(min_num)
        else:
            return -1