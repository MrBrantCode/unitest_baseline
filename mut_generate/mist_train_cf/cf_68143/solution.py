"""
QUESTION:
Write a function `count_nums` that takes an array of integers as input and returns the number of elements where the sum of their signed digits is greater than zero and divisible by 4. If a number is negative, consider its first signed digit as negative.
"""

def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = -((-num // 10) * 10 + (num % 10))
        digits = [int(d) for d in str(abs(num))]
        total = sum(digits)
        if total > 0 and total % 4 == 0:
            count += 1
    return count