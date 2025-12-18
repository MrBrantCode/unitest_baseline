"""
QUESTION:
Write a function `access_tuple_element(T, k)` that takes a tuple T and a positive integer k as parameters and returns the element at index k in T. The tuple T can contain elements of any data type and can be any positive integer length. The index k will always be a positive integer less than or equal to the length of T. Implement the logic without using built-in Python functions like `tuple.index()` or `tuple.__getitem__()`. The solution should have a time complexity of O(1).
"""

def access_tuple_element(T, k):
    return T[k-1]