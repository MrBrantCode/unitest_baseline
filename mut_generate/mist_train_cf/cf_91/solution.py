"""
QUESTION:
Create a function called `is_prime` that takes a number as input and returns True if the number is prime and False otherwise. Using this function, write a program that generates a list of all prime numbers between 1 and 10,000, calculates the sum of these prime numbers, and calculates the average of these prime numbers. The program should also count the total number of prime numbers found. The input range of 1 to 10,000 is fixed and does not need to be accepted as input.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True