"""
QUESTION:
Design a function named `unique_elements` that takes an array of integers as input and returns an array containing the unique elements in ascending order. The function should achieve an O(n log n) time complexity, and note that a strictly O(1) space complexity is required, meaning no extra space proportional to the size of the input array should be used. The function should also handle edge cases, including an empty input array and arrays containing negative numbers.
"""

def unique_elements(arr):
    if not arr:
        return []
    arr.sort()
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]