"""
QUESTION:
Create a function named `fib_primes(n)` that calculates the product of all Fibonacci prime numbers within the sequence of the first n numbers. The function should generate the Fibonacci sequence up to n numbers, select the prime numbers from the sequence, and return their product.
"""

def fib_primes(n):
    def is_prime(num):
        if num < 2:  
            return False
        for i in range(2, int(num**0.5)+1):  
            if num % i == 0:  
                return False
        return True  

    fib_seq = [0, 1]  
    for i in range(2, n):  
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    fib_primes = [num for num in fib_seq if is_prime(num)]  
    result = 1
    for num in fib_primes:
        result *= num
    return result