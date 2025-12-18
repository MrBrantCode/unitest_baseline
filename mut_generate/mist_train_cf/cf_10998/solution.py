"""
QUESTION:
Create a function `sum_of_prime_factors(N)` that takes a positive integer `N` greater than 1 and returns the sum of all its prime factors. The function should use a while loop to find the prime factors of `N` and add them together. Note that the input `N` is guaranteed to be a positive integer greater than 1.
"""

def sum_of_prime_factors(N):
    sum = 0
    i = 2
    while N > 1:
        if N % i == 0:
            sum += i
            N /= i
        else:
            i += 1
    return sum