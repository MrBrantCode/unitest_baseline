"""
QUESTION:
Implement a function `get_sublist(lst, threshold, divisor)` that takes a list `lst` and two integers `threshold` and `divisor` as input. The function should return a new list containing all elements from `lst` that are greater than `threshold` and divisible by `divisor`. The solution must not use built-in functions like `filter()` or list comprehensions.
"""

def get_sublist(lst, threshold, divisor):
    sublist = []
    for element in lst:
        if element > threshold and element % divisor == 0:
            sublist.append(element)
    return sublist