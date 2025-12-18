"""
QUESTION:
Create a function `sumEvenToN` that takes an integer `n` as input and returns the sum of all prime even numbers from 2 to `n`. The function should only consider even numbers that are prime, meaning they are only divisible by 1 and themselves. The input `n` is not restricted to any specific range.
"""

def sumEvenToN(n):
    prime_sum = 0
    for num in range(2, n + 1, 2):
        is_prime = True
        if num < 2:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_sum += num
    return prime_sum