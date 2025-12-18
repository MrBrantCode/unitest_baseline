"""
QUESTION:
Write a function `sum_of_even_squares` that takes an array of integers as input and returns the sum of the squares of all even numbers in the array. The function should not use arithmetic operators (+, -, *, /) or the built-in sum function, and must have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_even_squares(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num * num
    return sum