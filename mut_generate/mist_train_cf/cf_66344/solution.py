"""
QUESTION:
Write a function named `compute_gcd_for_fibonacci` that takes an integer `n` as input and returns the greatest common divisor (GCD) of all Fibonacci numbers up to `n`. Assume `n` is a positive integer greater than or equal to 2. The function should be designed with the understanding that the GCD of all Fibonacci numbers is always 1, but it should also be able to calculate the GCD in case this property is ignored.
"""

def compute_gcd_for_fibonacci(n):
    """
    This function will return the greatest common divisor (GCD)
    of Fibonacci series upto given number 'n'
    """
    # Create a Fibonacci sequence.
    fib_seq = [0, 1]
    i = 1
    while fib_seq[i] < n:
        fib_seq.append(fib_seq[i] + fib_seq[i-1])
        i += 1

    # Calculate the GCD of Fibonacci series.
    gcd = 1
    for i in range(len(fib_seq)):
        gcd = find_gcd(gcd, fib_seq[i])
    return gcd

def find_gcd(x, y):
    """
    This function implements the Euclidian algorithm to find GCD of two numbers 
    """
    while(y):
        x, y = y, x % y   
    return x