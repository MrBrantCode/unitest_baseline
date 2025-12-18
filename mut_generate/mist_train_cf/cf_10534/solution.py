"""
QUESTION:
Create a function named `fibonacci` that generates the first n elements of the Fibonacci sequence, where n is a prime number. The function should take an integer n as input and return a list of the first n Fibonacci numbers if n is prime. If n is not prime, the function should print "n is not a prime number" and not return anything.
"""

def fibonacci(n):
    """
    Generate the first n elements of the Fibonacci sequence if n is prime.

    Args:
        n (int): The number of elements in the Fibonacci sequence.

    Returns:
        list: A list of the first n Fibonacci numbers if n is prime.
        None: If n is not prime, print a message and return None.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not is_prime(n):
        print("n is not a prime number.")
        return None

    fib_sequence = []
    a, b = 0, 1
    count = 0
    while count < n:
        fib_sequence.append(a)
        a, b = b, a + b
        count += 1
    return fib_sequence