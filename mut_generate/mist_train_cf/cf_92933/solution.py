"""
QUESTION:
Create a function called `fibonacci` that generates an array containing the first `n` numbers of the Fibonacci sequence and returns the array. The function should take an integer `n` as a parameter and return the corresponding Fibonacci sequence array. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def fibonacci(n):
    """
    Generates an array containing the first n numbers of the Fibonacci sequence.

    Args:
    n (int): The number of elements in the Fibonacci sequence.

    Returns:
    list: An array containing the first n numbers of the Fibonacci sequence.
    """
    fib_array = [0, 1]  # Initial two numbers of the Fibonacci sequence

    for i in range(2, n):
        fib_array.append(fib_array[i-1] + fib_array[i-2])  # Add the next Fibonacci number to the array

    return fib_array