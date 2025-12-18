"""
QUESTION:
Create a function named `count_nums` that accepts an array of integers as an argument. The function should return the count of those elements where the sum of their signed digits is a perfect multiple of 4 and greater than zero. The first digit of a negative number should be considered as negative.
"""

def count_nums(nums):
    count = 0
    for num in nums:
        digits = [int(d) for d in str(abs(num))]
        if num < 0:
            digits[0] *= -1

        if sum(digits) % 4 == 0 and sum(digits) > 0:
            count += 1

    return count