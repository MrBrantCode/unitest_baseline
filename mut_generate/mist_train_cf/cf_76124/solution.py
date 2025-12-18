"""
QUESTION:
Write a function `prod_signs(arr)` that takes an array of integers as input and returns the sum of the magnitudes of unique integers multiplied by the combined product of signs for each distinctive number in the array. The function should ignore non-integer values, consider only non-zero integers, and eliminate repeated elements. If the array is empty or contains only zeros, the function should return None.
"""

def prod_signs(arr):
    if not arr or all(x == 0 for x in arr):  
        return None

    unique_elems = set(abs(x) for x in arr if x != 0)  
    result = 0

    for elem in unique_elems:
        sign_count = sum(1 if x == elem else -1 if x == -elem else 0 for x in arr)
        sign_sum = sign_count * elem
        result += sign_sum

    return result