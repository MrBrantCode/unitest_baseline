"""
QUESTION:
Write a function named `sum_of_digits` that takes an integer `num` and returns the sum of its digits. Then use this function to find the number of numbers from 1 to a given integer `N` where the sum of their digits is divisible by a given integer `M`. The function should not take any arguments. The values of `N` and `M` will be provided as input.
"""

def entance(N, M):
    def sum_of_digits(num):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum

    count = 0
    for num in range(1, N+1):
        digit_sum = sum_of_digits(num)
        if digit_sum % M == 0:
            count += 1
    return count