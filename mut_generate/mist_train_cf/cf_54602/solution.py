"""
QUESTION:
Design a function `fibonacci_seq(n, y)` that generates a Fibonacci sequence up to a limit of 'y' using the first 'n' prime numbers as seed values. The sequence should stop when 'n' prime numbers have been exhausted or the given number 'y' has been reached, whichever comes first. The first two prime numbers used should be 2 and 3.
"""

def fibonacci_seq(n, y):
    def prime_generator():
        yield 2
        yield 3

        primes = [2, 3]
        number = 5
        while True:
            if all(number % p > 0 for p in primes):
                primes.append(number)
                yield number
            number += 2

    prime_gen = prime_generator()
    Fibonacci_Sequence = [next(prime_gen) for _ in range(n)]
    while len(Fibonacci_Sequence) < n and Fibonacci_Sequence[-1] < y:
        Fibonacci_Sequence.append(Fibonacci_Sequence[-1] + Fibonacci_Sequence[-2])
        if Fibonacci_Sequence[-1] > y:
            Fibonacci_Sequence.pop() 
            break
    return Fibonacci_Sequence