"""
QUESTION:
Write a function `access_tuple_element(T, k)` that takes in a tuple T and an index k as parameters, and returns the element at index k. The tuple T may contain elements of any data type, and its length can be any positive integer. The index k will always be a positive integer less than or equal to the length of the tuple T. Do not use built-in Python functions like `tuple.index()` or `tuple.__getitem__()` to access the element; instead, implement the logic using loops or another method with a time complexity of O(1).
"""

def access_tuple_element(T, k):
    return T[k-1]