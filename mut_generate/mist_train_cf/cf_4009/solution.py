"""
QUESTION:
Write a function `recursive_product` that computes the product of a list of integers recursively, without using built-in functions or operators for multiplication. The function should handle edge cases such as an empty list, a list with only one element, and a list with negative numbers.

The function should have a time complexity of O(n), where n is the length of the input list, and should not use any additional data structures or variables to store intermediate results. 

The input is a list of integers `lst` with a length between 0 and 10^6, and the output is an integer representing the product of the list elements.
"""

def recursive_product(lst):
    def multiply(a, b):
        result = 0
        is_negative = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        for _ in range(b):
            result += a
        return -result if is_negative else result

    def helper(lst):
        if not lst:
            return 1
        return multiply(lst[0], helper(lst[1:]))

    return helper(lst)