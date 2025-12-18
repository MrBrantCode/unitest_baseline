"""
QUESTION:
Create a function named five_nine_twelve that takes an integer n as input and returns the total number of integers under n that meet the following conditions: contain the digit 5, can be evenly divided by either 9 or 12, and have a sum of digits divisible by 3. The function should only consider integers less than n.
"""

def five_nine_twelve(n: int) -> int:
    def contains_digit_5(num: int) -> bool:
        return '5' in str(num)

    def divisible_by_9_or_12(num: int) -> bool:
        return num % 9 == 0 or num % 12 == 0

    def sum_of_digits_divisible_by_3(num: int) -> bool:
        return sum(map(int, str(num))) % 3 == 0

    count = 0
    for i in range(n):
        if contains_digit_5(i) and divisible_by_9_or_12(i) and sum_of_digits_divisible_by_3(i):
            count += 1
    return count