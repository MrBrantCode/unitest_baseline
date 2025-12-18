"""
QUESTION:
Write a function called `remove_element` that takes two parameters: an array of integers `arr` and an integer `remove_element`. The function should return a new array that includes all elements from `arr` except `remove_element`.
"""

def remove_element(arr, remove_element):
    return [x for x in arr if x != remove_element]