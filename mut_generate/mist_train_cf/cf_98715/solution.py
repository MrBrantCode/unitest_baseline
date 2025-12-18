"""
QUESTION:
Design a function `is_prime` that checks whether a given number is prime or not and use it to generate the first 10 prime numbers between 1000 and 2000. Then, calculate the sum of their digits and convert the sum to binary. Output the prime numbers in a table format and display the binary representation of the sum of their digits.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True