"""
QUESTION:
Write a function `rearrange_array(arr)` that rearranges the input array of integers into an alternate order of even and odd elements, with no restrictions on the relative order of the original elements. The function should return the rearranged array.
"""

def rearrange_array(arr):
    evens = [e for e in arr if e % 2 == 0]
    odds = [o for o in arr if o % 2 != 0]
    result = []
    while evens or odds:
        if evens:
            result.append(evens.pop(0))
        if odds:
            result.append(odds.pop(0))
    return result