"""
QUESTION:
Create a function called `fibonacci(n)` that generates a modified Fibonacci sequence where each term is between 1 and 1000, inclusive. If a term exceeds 1000, subtract 1000 from it until it's within the range. The function should return the nth term of this sequence. Note that term indexing is base-1 (i.e., the first term is at index 1).
"""

def entrance(n):
    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        new_value = (fib_sequence[-1] + fib_sequence[-2]) % 1000
        new_value = new_value if new_value != 0 else 1000
        fib_sequence.append(new_value)
    return fib_sequence[n-1]