"""
QUESTION:
Write a function named increment_and_append that increments each element in the input array by 1 and appends 4 to the end of the array. The function should achieve a time complexity of O(n), where n is the length of the input array.
"""

def increment_and_append(arr):
    for i in range(len(arr)):
        arr[i] += 1
    arr.append(4)
    return arr