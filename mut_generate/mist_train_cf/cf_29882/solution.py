"""
QUESTION:
Write a function `product_sans_n(nums)` that takes a list of integers `nums` as input. The function should return a new list where each element is the product of all the elements in the input list except for the element at that index. If there are two or more occurrences of the integer 0 in the input list, the function should return a list of zeros of the same length as the input list. If there is exactly one occurrence of the integer 0 in the input list, the function should return a new list where the element at the index of 0 in the input list is replaced by the product of all the other elements, and all other elements are 0. The function signature is `def product_sans_n(nums: List[int]) -> List[int]`.
"""

from typing import List

def product_sans_n(nums: List[int]) -> List[int]:
    def product(arr: List[int]) -> int:
        total = 1
        for num in arr:
            if num != 0:
                total *= num
        return total

    if nums.count(0) >= 2:
        return [0] * len(nums)
    elif nums.count(0) == 1:
        temp = [0] * len(nums)
        temp[nums.index(0)] = product(nums)
        return temp
    res = product(nums)
    return [res // i if i != 0 else 0 for i in nums]