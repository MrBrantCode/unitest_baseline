"""
QUESTION:
Create a function called `rearrange_cyclic` that takes a non-empty array of integers as input and returns a new array. The function should rearrange the input array elements in a cyclical fashion, skipping any element that is divisible by 3. The rearrangement should start with the element at index 1, followed by the element at index 0, then the element at index 2 (if not skipped), and so on, wrapping around to the beginning of the array as necessary.
"""

def rearrange_cyclic(array):
    result = []
    n = len(array)
    for i in range(1, n + 1):
        if array[i % n] % 3 == 0:
            continue
        result.append(array[(i - 1) % n])
    return result