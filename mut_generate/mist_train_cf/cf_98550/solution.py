"""
QUESTION:
Write a function `even_numbers(start, end)` that takes two integers `start` and `end` as inputs, representing a range of numbers, and returns a list of even numbers within the range that are not divisible by 10 along with their sum. The function should include all numbers from `start` to `end` inclusive. Assume that `start` and `end` are integers and `start` is less than or equal to `end`.
"""

def entrance(start, end):
    even_nums = []
    even_sum = 0
    for num in range(start, end+1):
        if num % 2 == 0 and num % 10 != 0:
            even_nums.append(num)
            even_sum += num
    return even_nums, even_sum