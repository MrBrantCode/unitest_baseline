"""
QUESTION:
Implement a function `product_of_array(arr)` that calculates the product of all elements in the array `arr` without using loops, recursion, or built-in functions such as `reduce` or `product`. The solution should achieve a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return eval('*'.join(map(str, arr)))