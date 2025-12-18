"""
QUESTION:
Create a function `foo(nums_data)` that takes an array of integers `nums_data` as input. For each number in `nums_data`, add 2 to it, then filter out the resulting prime numbers from the array while maintaining the original sequence of numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def foo(nums_data):
    result = []
    for numeric_val in nums_data:
        numeric_val += 2
        result.append(numeric_val)
    return list(filter(is_prime, result))