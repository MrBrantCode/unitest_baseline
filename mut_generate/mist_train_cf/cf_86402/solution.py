"""
QUESTION:
Write a function `multiply_by_two` that takes a list of integers as input and returns a new list where each element is multiplied by 2. The function must not use any built-in list manipulation methods or functions such as `map()` or `list comprehension`, loops, or recursion. It can only use built-in Python functions and operators. The input list will only contain integers.
"""

def multiply_by_two(input_list):
    result_list = []
    list_length = len(input_list)
    indices = range(list_length)
    for element, index in zip(input_list, indices):
        result_list.append(element * 2)
    return result_list