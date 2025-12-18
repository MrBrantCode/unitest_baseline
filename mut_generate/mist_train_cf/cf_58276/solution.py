"""
QUESTION:
Write a function `divisor_count_and_list(n)` that takes a positive integer `n` as input and returns a tuple. The tuple should contain a boolean indicating whether the count of divisors of `n` is even, and a sorted list of those divisors. The function should handle the edge cases where `n` is negative or zero by returning an error message. The function should be optimized to handle large numbers efficiently.
"""

def divisor_count_and_list(n):
    if n < 1:
        return "Input must be a positive integer."

    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)

    return len(divisors) % 2 == 0, sorted(list(divisors))