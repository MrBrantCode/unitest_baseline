"""
QUESTION:
Write a function `sum_even_elements` that takes a list of positive integers as input and returns the sum of the even elements that are less than or equal to 10. The function should have a time complexity of O(n) and should not use any built-in sum or filter functions.
"""

def sum_even_elements(nums):
    sum_even = 0
    for num in nums:
        if num % 2 == 0 and num <= 10:
            sum_even += num
    return sum_even