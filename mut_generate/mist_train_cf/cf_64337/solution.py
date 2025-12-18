"""
QUESTION:
Design a function called `find_max_divisors` that accepts a list of distinct positive integers. The function should return the number with the most divisors. If multiple numbers have the maximum divisor count, return the smallest one.
"""

def find_max_divisors(numbers):
    def count_divisors(n):
        return sum(1 for i in range(1, int(n ** 0.5) + 1) if n % i == 0) * 2

    max_divisors = max(numbers, key=count_divisors)
    max_count = count_divisors(max_divisors)

    return min(x for x in numbers if count_divisors(x) == max_count)