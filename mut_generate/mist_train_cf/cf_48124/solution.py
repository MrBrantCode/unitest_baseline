"""
QUESTION:
Create a function named `checkPerfectNumber` that determines if a given integer `num` is a perfect number, defined as the sum of its divisors excluding the number itself. The function should return `True` if `num` is a perfect number and `False` otherwise. The input `num` is constrained to the range `1 <= num <= 10^8`.
"""

def checkPerfectNumber(num: int) -> bool:
    if num <= 1:
        return False
    sum_of_divisors = 1  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i * i != num:
                sum_of_divisors += num // i
    return sum_of_divisors == num