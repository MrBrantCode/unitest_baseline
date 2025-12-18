"""
QUESTION:
Create a function `interleave_reverse(arr1, arr2)` that takes two arrays `arr1` and `arr2` as input and returns a new array. The function should interleave the elements of `arr1` and `arr2` one by one, and then reverse the order of the elements in the resulting array. If one array is longer than the other, the remaining elements from the longer array should be appended to the end of the interleaved array.
"""

def interleave_reverse(arr1, arr2):
    interleaved = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            interleaved.append(arr1[i])
        if i < len(arr2):
            interleaved.append(arr2[i])
    return interleaved[::-1]