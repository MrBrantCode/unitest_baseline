"""
QUESTION:
Write a function `even_numbers(start, end)` that takes two integers as inputs, representing a range of numbers. The function should return a list of even numbers within the range, excluding any numbers that are divisible by 10, and the sum of all the even numbers in the list. The function should work for integer inputs only and assumes that the `start` input is less than or equal to the `end` input.
"""

def entrance(start, end):
    even_nums = []
    even_sum = 0
    for num in range(start, end+1):
        if num % 2 == 0 and num % 10 != 0:
            even_nums.append(num)
            even_sum += num
    return even_nums, even_sum