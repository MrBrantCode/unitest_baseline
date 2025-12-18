"""
QUESTION:
Construct a function `construct_spiral` that takes a positive integer `n`, a pattern type (`prime` or `fibonacci`), and an optional number of extra elements. The function should construct a spiral structure with `n` rotations, where each rotation is created from elements. The quantity of elements for following rotations depends on the pattern type and the number of elements from the previous rotation. If the pattern type is `prime`, the next prime number is appended to the existing elements from the prior rotation. For a `fibonacci` pattern type, the subsequent Fibonacci number is added to the last rotation's element count. The function should return a list detailing the element counts for each rotation.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = round(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    prime_candidate = n + 1
    while not is_prime(prime_candidate):
        prime_candidate += 1
    return prime_candidate

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

def construct_spiral(n, pattern, extra=0):
    elements = [n + extra]
    for _ in range(n - 1):
        if pattern == 'prime':
            elements.append(next_prime(elements[-1]))
        elif pattern == 'fibonacci':
            elements.append(fibonacci(len(elements) + 1) + extra)
    return elements