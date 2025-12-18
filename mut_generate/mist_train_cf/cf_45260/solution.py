"""
QUESTION:
Create a function `rearrange_four_elements(arr)` that takes a list of integers `arr` as input and returns a boolean value. The function should check if it's possible to rearrange the array in non-decreasing order by performing a right shift operation any number of times and swapping exactly two elements up to four times. The rearranged array should have an even number of elements lesser than the initial first element of the array, the sum of these lesser elements should be a perfect square, and the number of these elements should be prime. If the array is empty, return True.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.isqrt(n)+1, 2):
        if n%i == 0:
            return False
    return True

def is_perfect_square(n):
    if n < 1:
        return False
    root = math.isqrt(n)
    return root * root == n

def rearrange_four_elements(arr):
    if not arr:
        return True
    if len(arr) < 5:
        return False
    
    arr.sort()

    first_element = arr[0]
    lesser_elements = [i for i in arr if i < first_element]
    sum_lesser = sum(lesser_elements)

    if len(lesser_elements) % 2 != 0 or not is_prime(len(lesser_elements)) or not is_perfect_square(sum_lesser):
        return False

    return True