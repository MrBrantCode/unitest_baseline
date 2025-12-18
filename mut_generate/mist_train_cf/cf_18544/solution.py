"""
QUESTION:
Delete all occurrences of a given element from an array in-place without using any extra space or built-in functions. The function should have a time complexity of O(n) and be able to handle arrays with a maximum length of 10^6 elements containing integers within the range of -10^9 to 10^9.

The function name is `delete_occurrences(arr, element)`, where `arr` is the input array and `element` is the integer to be deleted.
"""

def delete_occurrences(arr, element):
    i = 0
    while i < len(arr):
        if arr[i] == element:
            # Shift all elements after the current index to the left
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            # Reduce the length of the array by 1
            arr.pop()
        else:
            i += 1
    return arr