"""
QUESTION:
Given a non-sequenced array of integers, create a function called `find_earliest_absent_positive` that identifies the earliest absent positive integer within the array. The function should return the smallest positive integer that is not present in the array. If the array is empty or contains no positive integers, the function should return 1.
"""

def find_earliest_absent_positive(array):
    if not array:
        return 1

    array = list(filter(lambda x: x > 0, array))
    array_length = len(array)

    if array_length == 0:
        return 1

    for i in range(array_length):
        num = abs(array[i])

        if num <= array_length:
            array[num - 1] = - abs(array[num - 1])

    for i in range(array_length):
        if array[i] > 0:
            return i + 1

    return array_length + 1