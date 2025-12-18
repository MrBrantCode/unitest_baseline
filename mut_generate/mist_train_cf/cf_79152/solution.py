"""
QUESTION:
Write a function `prod_signs(arr)` that calculates the total of unique non-zero integers' absolute values in the given array, each multiplicatively associated with the overall product of their corresponding signs. The array can contain nested arrays and non-zero integers. If the array is empty, non-existent, or contains other data types apart from integers or nested arrays of integers, the function should return None.
"""

def prod_signs(arr):
    def flatten(lis):
        for item in lis:
            if isinstance(item, list):
                for sub_item in flatten(item):
                    yield sub_item
            else:
                yield item

    def multiply_signs(lis):
        sign = 1
        for i in lis:
            if i < 0:
                sign *= -1
        return sign

    if not arr or not all(isinstance(i, (int, list)) for i in arr):
        return None
    flat_arr = list(flatten(arr))
    if any(isinstance(i, str) for i in flat_arr):
        return None
    unique_values = set(abs(i) for i in flat_arr if i != 0)
    total = sum(unique_values)
    sign = multiply_signs(flat_arr)
    return None if 0 in flat_arr else total * sign