"""
QUESTION:
Write a function named `fib_and_prime(k)` that takes an integer `k` as input and returns a tuple containing the kth element in the Fibonacci sequence and a boolean indicating whether the kth element is a prime number. The Fibonacci sequence starts with 0 and 1. The function should have a time complexity of O(k + sqrt(n)) where n is the kth Fibonacci number, and a space complexity of O(1), where n is the kth Fibonacci number and k is the input.
"""

def fib_and_prime(k):
    """
    This function generates the kth element in the Fibonacci sequence 
    and checks whether the kth element is a prime number.
    
    Args:
    k (int): The position of the Fibonacci number to be generated.
    
    Returns:
    tuple: A tuple containing the kth element in the Fibonacci sequence 
           and a boolean indicating whether the kth element is a prime number.
    """
    # Generate the kth Fibonacci number
    if k <= 0:
        return "Input should be a positive integer."
    elif k == 1:
        fib_k = 0
    elif k == 2:
        fib_k = 1
    else:
        a, b = 0, 1
        for _ in range(2, k):
            a, b = b, a + b
        fib_k = b
    
    # Check whether the kth Fibonacci number is a prime number
    if fib_k <= 1:
        is_prime_k = False
    elif fib_k == 2:
        is_prime_k = True
    else:
        is_prime_k = all(fib_k % i != 0 for i in range(2, int(fib_k ** 0.5) + 1))
    
    return fib_k, is_prime_k