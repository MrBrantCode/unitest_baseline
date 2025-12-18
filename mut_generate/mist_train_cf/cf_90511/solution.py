"""
QUESTION:
Create a function `rotate_array(arr, positions)` that rotates the given array `arr` to the right by `positions` places. The function should handle both positive and negative values for `positions`. The time complexity should be O(n), where n is the length of the array. The function should not use built-in array manipulation functions and should rotate the array in place without creating a new array.
"""

def rotate_array(arr, positions):
    if len(arr) <= 1:
        return arr

    # Normalize the number of positions
    positions = positions % len(arr)

    if positions == 0:
        return arr

    if positions < 0:
        positions = len(arr) + positions

    # Reverse the entire array
    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse_array(0, len(arr)-1)
    reverse_array(0, positions-1)
    reverse_array(positions, len(arr)-1)

    return arr