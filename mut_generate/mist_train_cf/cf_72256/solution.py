"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the 'n'th term and calculates the sum of the even numbered Fibonacci terms up to 'n'th term. The function should accept a single parameter 'n', which must be a non-negative integer. If 'n' is not a non-negative integer, the function should return an error message. The function should return a list containing the Fibonacci sequence and the sum of even numbered terms. The function should be optimized for larger values of 'n'.
"""

def fibonacci(n):
    # Validate input
    if type(n) != int or n < 0:
        return "Error. The input 'n' must be a non-negative integer."
        
    if n == 0:
        return [[0], 0]  # Returning [Fibonacci sequence, sum of evens]
    elif n == 1:
        return [[0, 1], 0]

    fib_sequence = [0, 1]
    even_sum = 0

    for i in range(2, n + 1):
        new_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(new_value)

        if new_value % 2 == 0:  # checking if even
            even_sum += new_value

    return [fib_sequence, even_sum]