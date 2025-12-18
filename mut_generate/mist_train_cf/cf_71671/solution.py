"""
QUESTION:
Create a function `fibonacci_primes(n)` that generates the Fibonacci sequence up to the nth number, identifies the prime numbers in the sequence, and returns the prime numbers in descending order.
"""

def fibonacci_primes(n):
    num1, num2 = 0, 1
    sequence = [num2]
  
    # Calculate Fibonacci sequence
    for i in range(n-1):
        num1, num2 = num2, num1 + num2
        sequence.append(num2)

    # Function to check if a number x is prime
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    # Find prime numbers in the sequence
    primes = [x for x in sequence if is_prime(x)]
  
    # Sort the primes in descending order and return
    return sorted(primes, reverse=True)