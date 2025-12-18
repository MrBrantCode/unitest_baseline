"""
QUESTION:
Write a function called `separate_numbers` that takes a list of integers as input and returns three lists of numbers. The first list should contain numbers that are divisible by 2, the second list should contain numbers that are not divisible by 2, and the third list should contain numbers that are divisible by 2 and have a digit sum greater than 10. You are not allowed to use any built-in functions or libraries for determining divisibility or calculating digit sum.
"""

def separate_numbers(lst):
    """
    Separate numbers in a list into three lists: numbers divisible by 2, 
    numbers not divisible by 2, and numbers divisible by 2 with a digit sum greater than 10.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: Three lists of numbers.
    """
    divisible_by_2 = []
    not_divisible_by_2 = []
    divisible_by_2_digit_sum_greater_than_10 = []

    def is_divisible_by_2(n):
        return n % 2 == 0

    def digit_sum(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        return sum

    for num in lst:
        if is_divisible_by_2(num):
            divisible_by_2.append(num)
            if digit_sum(num) > 10:
                divisible_by_2_digit_sum_greater_than_10.append(num)
        else:
            not_divisible_by_2.append(num)

    return divisible_by_2, not_divisible_by_2, divisible_by_2_digit_sum_greater_than_10