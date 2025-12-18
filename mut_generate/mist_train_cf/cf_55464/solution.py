"""
QUESTION:
Create a function called `product_fib_sequence` that calculates the product of all Fibonacci numbers within a given range, where the range is specified by two parameters `start_range` and `end_range` (zero-based indexing). The function should generate the Fibonacci sequence up to the `end_range` and then calculate the product of the numbers within the specified range.
"""

def product_fib_sequence(start_range, end_range):
    fib_sequence = [0, 1]
    for i in range(2, end_range+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    product = 1
    for num in fib_sequence[start_range:end_range+1]:
        product *= num
    return product