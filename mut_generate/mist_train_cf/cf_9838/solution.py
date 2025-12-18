"""
QUESTION:
Write a function called `count_primes` that takes a list of integers as input and returns the number of prime numbers in the list. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. The function should count prime numbers in the list and return the total count.
"""

def count_primes(numbers):
    count = 0
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    break
            else:
                count += 1
    return count