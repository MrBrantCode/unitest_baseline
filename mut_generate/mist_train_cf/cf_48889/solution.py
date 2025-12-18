"""
QUESTION:
Generate a function `fibonacci(n)` that returns the Fibonacci sequence up to the nth number. Then, create a function `check_prime(num)` that checks if a given number is prime. Use these functions to find the Fibonacci sequence up to the 10th number and identify the prime numbers in the sequence. The solution should be efficient in terms of time and space complexity.
"""

def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth number."""
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers

def check_prime(num):
    """Check if a given number is prime."""
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           return True

    return False