"""
QUESTION:
Create a function `multiply_elements` that takes a number `num` and a list `lst` of positive integers, and returns a new list where each element from `lst` is multiplied by `num`. The function should have a time complexity of O(n), where n is the length of the list.
"""

def multiply_elements(num, lst):
    return [num * element for element in lst]