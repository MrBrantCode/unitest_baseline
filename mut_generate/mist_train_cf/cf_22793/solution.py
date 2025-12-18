"""
QUESTION:
Write a function `product_of_array(arr)` that calculates the product of all elements in a given array. The function should not use any loops, recursion, or built-in functions such as `reduce` or `product`. It should achieve a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. The function should also handle the case where the input array is empty.
"""

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return eval('*'.join(map(str, arr)))