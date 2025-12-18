"""
QUESTION:
Create a function `sub_array(array, num)` that takes an array and a number `num` as input, and returns a new array with all occurrences of `num` removed. The function should not use the `remove()` method and have a time complexity of O(n), where n is the length of the array.
"""

def sub_array(array, num):
    new_array = []
    for i in range(len(array)):
        if array[i] != num:
            new_array.append(array[i])
    return new_array