"""
QUESTION:
Write a function called `sum_even_integers` that calculates the sum of all even integers in the range of `m` to `n` (inclusive), where `m` and `n` are positive integers. The function should then check if the sum is a prime number and return the sum and a boolean indicating whether the sum is prime or not. The function should take two parameters, `m` and `n`, and should not take any other inputs.
"""

def sum_even_integers(m, n):
    sum_of_evens = 0
    for num in range(m, n + 1):
        if num % 2 == 0:
            sum_of_evens += num
            
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum_of_evens, is_prime(sum_of_evens)