"""
QUESTION:
Create a function named `sub_array` that takes an array and a number `num` as input. The function should return a new array containing all elements from the input array except the occurrences of `num`. The function should have a time complexity of O(n), where n is the length of the array, and should not use the `remove()` method.
"""

def sub_array(array, num):
    new_array = []
    for i in range(len(array)):
        if array[i] != num:
            new_array.append(array[i])
    return new_array