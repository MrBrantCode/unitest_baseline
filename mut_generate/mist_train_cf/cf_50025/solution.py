"""
QUESTION:
Write a function `prod_signs(arr)` that calculates the cumulative product of the signs and absolute values of unique non-zero integers in the given array. The function should return `None` if the array is empty or contains zero. The sign of each unique number is represented by 1 if positive, -1 if negative, and the product should be calculated accordingly.
"""

def prod_signs(arr):
    if not arr:  # check for empty list
        return None

    if 0 in arr:  # check if the array contains a zero
        return None

    signs = 1
    unique_set = set()

    for num in arr:
        # convert to absolute
        abs_num = abs(num)

        # calculate product of unique abosultes
        if abs_num not in unique_set:
            unique_set.add(abs_num)
            signs = signs * abs_num if num > 0 else -1 * signs * abs_num

    return signs