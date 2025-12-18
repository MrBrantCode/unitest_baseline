"""
QUESTION:
Create a function called `generatePrimeFibonacci(length)` that generates a Fibonacci sequence with a specified length, where each number in the sequence is a prime number. The function should return the generated Fibonacci sequence as a list of integers. The sequence should start from the first prime Fibonacci number. Note that the length of the sequence should be equal to the specified length.
"""

import math

def generatePrimeFibonacci(length):
    """
    Generate a Fibonacci sequence with a specified length, where each number in the sequence is a prime number.

    Args:
        length (int): The length of the Fibonacci sequence.

    Returns:
        list: A list of prime Fibonacci numbers.
    """
    def isPrime(number):
        """Check if a number is prime."""
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    fibonacciSequence = []
    a = 0
    b = 1
    while len(fibonacciSequence) < length:
        nextFibonacci = a + b
        if isPrime(nextFibonacci):
            fibonacciSequence.append(nextFibonacci)
        a, b = b, nextFibonacci
    return fibonacciSequence