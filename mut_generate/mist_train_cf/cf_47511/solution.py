"""
QUESTION:
Write a function `construct_spiral` that takes an integer `n`, a pattern (`'prime'` or `'fibonacci'`), and an optional argument `extra` denoting the number of extra components. The function should return a list specifying the components count for every curve in a spiral structure having `n` turns. The initial curve has `n` elements, and subsequent curves' components are contingent upon the pattern and components from the earlier rotation. If the pattern is `'prime'`, the next prime number is added to the previous components. If the pattern is `'fibonacci'`, the next Fibonacci number is added to the previous components. If `extra` is provided, it is added to the initial curve's components. The function should return a list where the element at position `i` denotes the components quantity in the `i+1` turn.
"""

def next_prime(num):
    while True:
        num += 1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return num


def construct_spiral(n, pattern, extra=0):
    elements = [n + extra]
    next_fib = n + extra
    previous_fib = n + extra
    for _ in range(n-1):
        if pattern == 'prime':
            next_p = next_prime(elements[-1])
            elements.append(next_p)
        elif pattern == 'fibonacci':
            add_fib = next_fib
            next_fib = previous_fib + next_fib
            previous_fib = add_fib
            elements.append(next_fib)
    return elements