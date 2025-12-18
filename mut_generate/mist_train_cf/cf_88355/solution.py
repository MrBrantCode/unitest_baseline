"""
QUESTION:
Implement a function `multiply_and_limit` that takes a list of integers `lst` and an integer `size` as input. The function should return a new list where each element in the input list is multiplied by three, but capped at the input `size`. If an element exceeds the `size`, it should be replaced with the `size`. The function should handle empty lists and have a time complexity of O(n), where n is the length of the input list, without using built-in Python functions like map, filter, or list comprehension, and using recursion to solve the problem.
"""

def multiply_and_limit(lst, size):
    if not lst:
        return []
    else:
        result = lst[0] * 3
        return [size if result > size else result] + multiply_and_limit(lst[1:], size)