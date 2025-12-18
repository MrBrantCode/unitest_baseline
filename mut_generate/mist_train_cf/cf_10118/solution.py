"""
QUESTION:
Create a function called `fibonacci_with_primes` that takes an integer `n` as input and prints the first `n` terms in the Fibonacci sequence. For each term, check if it's a prime number and print "prime" next to it if it is.
"""

def fibonacci_with_primes(n):
    fib_sequence = [0, 1]
    
    # Check if each term is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    # Print the terms with "prime" if they are prime
    for term in fib_sequence:
        if is_prime(term):
            print(term, "prime")
        else:
            print(term)