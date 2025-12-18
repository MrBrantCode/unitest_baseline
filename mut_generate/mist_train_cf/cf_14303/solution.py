"""
QUESTION:
Write a function `rearrange_divisible_by_3(arr)` that takes an array of integers as input and returns a rearranged array where all elements divisible by 3 come first, while maintaining the original relative order of elements.
"""

def rearrange_divisible_by_3(arr):
    divisible_by_3 = []
    not_divisible_by_3 = []

    for num in arr:
        if num % 3 == 0:
            divisible_by_3.append(num)
        else:
            not_divisible_by_3.append(num)

    return divisible_by_3 + not_divisible_by_3