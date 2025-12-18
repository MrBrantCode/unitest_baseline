"""
QUESTION:
Implement a function `is_prime(num)` that takes an integer as input and returns a boolean indicating whether the number is prime or not. The function should not use the modulus operator (%) to check for divisibility. Instead, implement a custom method to determine divisibility. Assume that the input number is a non-negative integer.
"""

def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False

    # Check divisibility starting from 2
    for i in range(2, int(num ** 0.5) + 1):
        # Subtract i from num until it becomes less than i
        temp = num
        while temp >= i:
            temp -= i

        # If temp becomes 0, it means num is divisible without remainder
        if temp == 0:
            return False

    return True