"""
QUESTION:
Write a function `insert_value(array, value, max_length)` that inserts a value at the end of an array if the resulting array does not exceed the maximum length. If the array would exceed the maximum length, remove the first element before inserting the new value. The function must not use built-in Python functions or methods, except for `len(array)`, and have a time complexity of O(1).
"""

def insert_value(array, value, max_length):
    if len(array) < max_length:
        array.append(value)
    else:
        array.pop(0)
        array.append(value)
    return array