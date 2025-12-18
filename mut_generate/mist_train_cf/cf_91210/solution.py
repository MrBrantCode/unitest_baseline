"""
QUESTION:
Construct a function `fibonacci_with_primes(n)` that prints the first n terms in a Fibonacci sequence. For each term, check if it is a prime number and print "prime" next to it if true. The function should not take any input other than the integer n.
"""

def fibonacci_with_primes(n):
    fib_sequence = [0, 1]
    
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    for term in fib_sequence:
        if is_prime(term):
            print(term, "prime")
        else:
            print(term)