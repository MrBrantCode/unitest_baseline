"""
QUESTION:
Write a function named `remove_duplicates` that takes an array of elements as input, removes any duplicate elements while maintaining their original order, and does not use any additional data structures. The function should only modify the input array and return the modified array without any duplicate elements.
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