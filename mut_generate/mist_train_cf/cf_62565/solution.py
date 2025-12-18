"""
QUESTION:
Create a function `get_even_fib` that generates and returns a list of even Fibonacci numbers within a given range of numbers (1 through `numbers`). The function should generate Fibonacci numbers up to the input limit and then return only the even numbers from the generated sequence.
"""

def get_even_fib(numbers):
    fib_sequence = [1, 2]
    while fib_sequence[-1] + fib_sequence[-2] <= numbers:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return [x for x in fib_sequence if x % 2 == 0]