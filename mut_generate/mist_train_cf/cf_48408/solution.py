"""
QUESTION:
Design a function named `sum_of_primes` that takes a multidimensional array of integers as input and returns the total sum of all prime numbers present in the array. The function should iterate through each number in the array and check if it is prime, then add it to the total sum if it is.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def sum_of_primes(arr):
    total = 0
    for row in arr:
        for num in row:
            if is_prime(num):
                total += num
    return total