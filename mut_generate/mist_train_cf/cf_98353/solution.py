"""
QUESTION:
Create a function named `unique_max` that takes a list of numbers and an optional boolean parameter `find_max` (defaulting to `True`). The function should return the index of the maximum or minimum number in the list, depending on the value of `find_max`. However, if the maximum or minimum number is not singularly unique, the function should return -1.
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