"""
QUESTION:
Write a function `prod_signs_orig(arr)` that calculates the cumulative sum of the absolute values of distinct non-zero integers in the input array, each multiplied by the total product of their occurrences in the array. The occurrences are represented by 1 if the integer is positive, -1 if the integer is negative, and excluded if the integer is zero. If the array is empty or contains no non-zero integers, the function should return None.
"""

def prod_signs(arr):
    if arr is None or len(arr) == 0:
        return None
    
    distinct_elements = set(filter(None, arr))
    
    if len(distinct_elements) == 0:
        return None

    sum_of_products = 0

    for element in distinct_elements:
        product_of_tags = arr.count(element) if element > 0 else -arr.count(element)
        sum_of_products += abs(element) * product_of_tags

    return sum_of_products