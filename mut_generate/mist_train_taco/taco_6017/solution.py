"""
QUESTION:
# Task
Given an integer array `arr`. Your task is to remove one element, maximize the product of elements. 

The result is the element which should be removed. If more than one valid results exist, return the smallest one.


# Input/Output


`[input]` integer array `arr`

non-empty unsorted integer array. It contains positive integer, negative integer or zero.

`3 ≤ arr.length ≤ 15`

`-10 ≤ arr[i] ≤ 10`

`[output]` an integer

The element that should be removed.

# Example

For `arr = [1, 2, 3]`, the output should be `1`.

For `arr = [-1, 2, -3]`, the output should be `2`.

For `arr = [-1, -2, -3]`, the output should be `-1`.

For `arr = [-1, -2, -3, -4]`, the output should be `-4`.
"""

def find_element_to_remove_for_max_product(arr):
    if arr.count(0) > 1:
        return min(arr)
    
    neg = [n for n in arr if n < 0]
    pos = [n for n in arr if n >= 0]
    
    if len(neg) % 2:
        return min(neg) if 0 in arr else max(neg)
    else:
        return min(pos) if pos else min(neg)