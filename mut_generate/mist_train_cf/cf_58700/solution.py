"""
QUESTION:
Construct a Python function named `prime_dict(limit)` that generates a dictionary where keys are unique prime numbers from 2 up to the given limit, and their corresponding values are the products of the prime numbers and their corresponding Fibonacci numbers. The function should handle edge cases where the limit is a non-positive integer by returning an error message.
"""

def prime_dict(limit):
    if limit <= 0:
        return "Limit must be a positive integer"
    my_dict = {}
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            a, b = 0, 1
            for _ in range(num - 1):
                a, b = b, a + b
            my_dict[num] = b * num  
    return my_dict