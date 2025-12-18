"""
QUESTION:
Create a function named `fibo_seq` that takes an integer `n` as input and returns a list of distinct Fibonacci numbers that are also prime, up to the given number `n`. The function should generate Fibonacci numbers up to `n`, then filter out non-prime numbers. The output should not contain any duplicate prime Fibonacci numbers.
"""

def fibo_seq(n):
    """
    This function generates distinct Fibonacci numbers that are also prime, up to the given number n.
    
    Args:
        n (int): The upper limit for generating Fibonacci numbers.
    
    Returns:
        list: A list of distinct prime Fibonacci numbers up to n.
    """
    
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    
    return list(set([num for num in fib if is_prime(num) and num <= n]))