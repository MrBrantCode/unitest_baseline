"""
QUESTION:
Implement a function called `multiply_and_limit` that takes a list of integers and the size of the list as input, and returns a new list where every element is multiplied by three and none of the elements exceed the size of the list. If any element exceeds the size of the list, it should be replaced with the size of the list. The function should handle cases where the input list is empty and return an empty list in such cases. The function must have a time complexity of O(n), cannot use built-in Python functions like map, filter, or list comprehension, and must use recursion to solve the problem.
"""

def multiply_and_limit(lst, size):
    if not lst:
        return []
    elif lst[0] * 3 > size:
        return [size] + multiply_and_limit(lst[1:], size)
    else:
        return [lst[0] * 3] + multiply_and_limit(lst[1:], size)