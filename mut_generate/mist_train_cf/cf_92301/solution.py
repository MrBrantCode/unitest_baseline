"""
QUESTION:
Create a function called `separate_numbers` that takes a list of integers as input. Separate the numbers into three lists: one for numbers divisible by 2, one for numbers not divisible by 2, and one for numbers divisible by 2 that also have a digit sum greater than 10. Do not use any built-in functions or libraries for determining divisibility or calculating digit sum.
"""

def separate_numbers(lst):
    """
    Separate the numbers in the list into three lists: one for numbers divisible by 2, 
    one for numbers not divisible by 2, and one for numbers divisible by 2 that also 
    have a digit sum greater than 10.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: Three lists of integers.
    """
    def is_divisible_by_2(n):
        # Check if a number is divisible by 2
        return n % 2 == 0

    def digit_sum(n):
        # Calculate the digit sum of a number
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        return sum

    divisible_by_2 = []
    not_divisible_by_2 = []
    divisible_by_2_digit_sum_greater_than_10 = []

    for num in lst:
        if is_divisible_by_2(num):
            divisible_by_2.append(num)
            if digit_sum(num) > 10:
                divisible_by_2_digit_sum_greater_than_10.append(num)
        else:
            not_divisible_by_2.append(num)

    return divisible_by_2, not_divisible_by_2, divisible_by_2_digit_sum_greater_than_10