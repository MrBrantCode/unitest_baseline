"""
QUESTION:
Create a function called `is_prime(n)` to check if a given number is prime with a time complexity of O(sqrt(n)). Do not use any built-in prime number checking functions or libraries. Use this function to implement other functions to calculate and print the following results:

- Print all prime numbers between 1 and 1000 in descending order.
- The sum of all prime numbers between 1 and 1000.
- The product of all prime numbers between 1 and 1000.
- The difference between the largest and smallest prime numbers between 1 and 1000.
- The average of all prime numbers between 1 and 1000.
- The two prime numbers with the largest difference between them.
- The prime number with the maximum number of divisors between 1 and 1000.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True