"""
QUESTION:
Create a generator function `solve` that takes a list of dictionaries `start_list` and an integer `limit` as input. The function should iterate over each dictionary in `start_list`, and for each dictionary, it should iterate over its key-value pairs. If a value is a Fibonacci number less than `limit`, the function should yield a tuple containing the dictionary index, key, and value.
"""

def solve(start_list, limit):
    fibo = set(fibonacci_seq(limit))
    return check_fibonacci(start_list, fibo)

def fibonacci_seq(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def check_fibonacci(dictionary, fibo):
    for index, pair in enumerate(dictionary):
        for k, v in pair.items():
            if v in fibo:
                yield (index, k, v)