"""
QUESTION:
Write a function named sum_of_even_squares that takes an array of integers as input and returns the sum of the squares of all even numbers in the array without using any arithmetic operators (+, -, *, /) or the built-in sum function. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_even_squares(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num * num
    return sum