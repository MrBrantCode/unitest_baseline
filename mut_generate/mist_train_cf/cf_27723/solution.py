"""
QUESTION:
Implement a function called `custom_map` that takes two arguments: a function `func` that takes a single argument and returns a transformed value, and a list `lst` of integers. The `custom_map` function should apply the `func` to each element of the `lst` and return a new list containing the transformed values without using the built-in `map` function or list comprehensions.
"""

def custom_map(func, lst):
    def apply_func_to_list(lst, result):
        if not lst:
            return result
        else:
            return apply_func_to_list(lst[1:], result + [func(lst[0])])

    return apply_func_to_list(lst, [])