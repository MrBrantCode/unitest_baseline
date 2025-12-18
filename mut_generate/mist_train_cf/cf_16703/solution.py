"""
QUESTION:
Construct a function named `fibonacci_prime` that takes an integer `n` as input, prints the first `n` terms in the Fibonacci sequence, checks each term to see if it is a prime number, and prints "prime" next to the term if it is prime. The function should also return the sum of all the prime terms in the Fibonacci sequence.
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

def fibonacci_prime(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib_seq = [1, 1]
    sum_primes = 0
    
    # Check if the first term is prime
    if is_prime(fib_seq[0]):
        print(fib_seq[0], "prime")
        sum_primes += fib_seq[0]
    else:
        print(fib_seq[0])
    
    # Check if the second term is prime
    if is_prime(fib_seq[1]):
        print(fib_seq[1], "prime")
        sum_primes += fib_seq[1]
    else:
        print(fib_seq[1])
    
    # Generate the remaining terms in the Fibonacci sequence
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        
        # Check if the term is prime
        if is_prime(fib_seq[i]):
            print(fib_seq[i], "prime")
            sum_primes += fib_seq[i]
        else:
            print(fib_seq[i])
    
    return sum_primes