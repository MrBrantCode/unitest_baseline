"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array as input and returns the array with duplicate elements removed while maintaining the original order of elements. The function should not use any additional data structures. The input array can contain duplicate elements and can be of any length, including 0 or 1 elements.
"""

def remove_duplicates(arr):
    length = len(arr)
    if length <= 1:
        return arr

    index = 1
    while index < length:
        inner_index = 0
        while inner_index < index:
            if arr[index] == arr[inner_index]:
                for i in range(index, length - 1):
                    arr[i] = arr[i + 1]
                length -= 1
                index -= 1
                break
            inner_index += 1
        index += 1

    return arr[:length]