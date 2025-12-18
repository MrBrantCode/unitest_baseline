"""
QUESTION:
Create a function `rearrange_cyclic` that takes an array of integers and rearranges the elements in a cyclical fashion, with the following rules: 
- The element at index 0 goes to the end of the array.
- Each subsequent element moves to the position immediately after the previous element, wrapping around to the beginning of the array if necessary.
- If the element at the current index is divisible by 3, it is skipped and the next element is considered for rearrangement.
"""

def rearrange_cyclic(array):
    result = []
    n = len(array)
    for i in range(1, n + 1):
        if array[i - 1] % 3 == 0:
            continue
        result.append(array[i % n])
    return result