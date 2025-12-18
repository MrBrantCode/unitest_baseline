"""
QUESTION:
Write a function `find_triangular_number_with_divisors` that returns the first triangular number that has more than a given threshold of divisors. A triangular number is a number that can be represented in the form of n(n+1)/2, where n is a positive integer. The function should use two helper functions: `get_triangular_number(n)` that takes an integer `n` as input and returns the `n`th triangular number, and `get_divisor_count(num)` that takes an integer `num` as input and returns the count of divisors for `num`. The function should return the first triangular number that has more than the given threshold of divisors.
"""

def find_triangular_number_with_divisors(divisor_count_threshold):
    def get_triangular_number(n):
        return n * (n + 1) // 2

    def get_divisor_count(num):
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 2
        if int(num**0.5) * int(num**0.5) == num:
            count -= 1
        return count

    i = 1
    while True:
        triangle = get_triangular_number(i)
        count = get_divisor_count(triangle)
        if count > divisor_count_threshold:
            return triangle
        i += 1