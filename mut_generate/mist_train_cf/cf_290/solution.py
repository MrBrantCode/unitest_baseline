"""
QUESTION:
Write a function `fibonacci_sequence(num_elements)` that generates the Fibonacci sequence up to `num_elements`. The function should first calculate `num_elements` by finding the sum of the first 5 prime numbers between 10 and 100. If `num_elements` is a negative number, display an error message and return. The function should return a list of Fibonacci numbers up to `num_elements`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(num_elements):
    if num_elements <= 0:
        print("Error: Please enter a positive number of elements to generate.")
        return

    primes = []
    count = 0
    num = 10

    while count < 5:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1

    num_elements = sum(primes)

    fib_sequence = [0, 1]
    for i in range(2, num_elements):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence