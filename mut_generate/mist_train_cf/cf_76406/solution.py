"""
QUESTION:
Create a function `xor_aggregate(arr)` that calculates the aggregate of bitwise exclusive OR operations performed on every possible pair of integers within the provided array. The function should handle edge cases where the array is empty or contains non-integer values. The function should not perform the XOR operation on an element with itself and should count each pair only once.
"""

def xor_aggregate(arr):
    if not arr:
        return 0
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if isinstance(arr[i], int) and isinstance(arr[j], int):
                result += arr[i] ^ arr[j]
    return 2 * result