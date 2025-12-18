"""
QUESTION:
Write a function named `find_prime_fibonacci` that takes an integer `n` as input, generates the first `n` numbers of the Fibonacci sequence, and returns a list of prime numbers present in the generated sequence. Assume that 0 and 1 are not prime numbers.
"""

def find_prime_fibonacci(n):
    def gen_fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(fib)
        return fib_sequence

    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fibonacci_sequence = gen_fibonacci(n)
    return [num for num in fibonacci_sequence if check_prime(num)]