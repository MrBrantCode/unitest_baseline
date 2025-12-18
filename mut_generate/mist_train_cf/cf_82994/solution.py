"""
QUESTION:
Create a function named `fibonacci_like_sequence` that generates a Fibonacci-like sequence up to a given number `n`. The sequence should start with the base pair `n` and the next prime number after `n`, and then each subsequent number is the sum of the previous two. The function should return a list of numbers in the sequence.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def fibonacci_like_sequence(n):
    base_pair = [n, next_prime(n)]
    sequence = []

    for i in range(n):
        if i < len(base_pair):
            sequence.append(base_pair[i])
        else:
            sequence.append(sequence[-1] + sequence[-2])

    return sequence