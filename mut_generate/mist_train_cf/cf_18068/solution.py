"""
QUESTION:
Write a function `multiply_array(arr)` that multiplies each element in the array with all other elements in the array. The function should not use any built-in Python functions or libraries and have a time complexity of O(n). The function should also use only constant extra space.
"""

def entrance(arr):
    n = len(arr)
    result = [0] * n
    product_all = 1
    zero_count = 0
    for num in arr:
        if num != 0:
            product_all *= num
        else:
            zero_count += 1

    for i in range(n):
        if zero_count > 1:
            result[i] = 0
        elif zero_count == 1:
            result[i] = product_all if arr[i] == 0 else 0
        else:
            result[i] = product_all // arr[i]
    return result