"""
QUESTION:
Write a function "count_nums" that takes an integer array as input and returns the count of elements whose sum of absolute values of digits (considering the sign of the number) is positive and divisible by 4.
"""

def count_nums(arr):
    def sum_digits(n):
        n = abs(n)
        total = 0
        while n > 0:
            n, remainder = divmod(n, 10)
            total += remainder
        return total

    return sum(sum_digits(i) % 4 == 0 for i in arr)