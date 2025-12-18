"""
QUESTION:
Write a function `sum_odd` that calculates the sum of all odd numbers between two given numbers, excluding sums that are prime numbers. The function takes two arguments: `lower` and `upper`, representing the lower and upper limits respectively. If `lower` is higher than `upper`, the function should return an error message. Both `lower` and `upper` must be positive numbers. The function should be efficient for large inputs.
"""

def sum_odd(lower, upper):
    if lower < 0 or upper < 0:
        return "Error: both lower limit and upper limit must be positive numbers"
    
    if lower > upper:
        return "Error: lower limit cannot be higher than upper limit"

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total_sum = 0
    for num in range(lower, upper + 1):
        if num % 2 != 0:  
            total_sum += num
            if is_prime(total_sum):  
                total_sum -= num
    return total_sum