"""
QUESTION:
Write a function `sum_divisible_by_5` that takes a list of integers as input and returns the sum of all numbers in the list that are divisible by 5 and not prime. The function should use the built-in `filter()` function to filter the list. The input list contains numbers less than 1000.
"""

def sum_divisible_by_5(nums):
    def is_divisible_by_5(num):
        return num % 5 == 0

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    filtered_list = filter(is_divisible_by_5, nums)
    filtered_list = filter(lambda x: not is_prime(x), filtered_list)

    return sum(filtered_list)