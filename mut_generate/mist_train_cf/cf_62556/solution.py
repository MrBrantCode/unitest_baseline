"""
QUESTION:
Create a function `fib(n)` to calculate the nth Fibonacci number without using any looping structures or arrays. The function should have a linear time complexity. The Fibonacci sequence is defined where each number is the sum of the two preceding ones, starting from 0 and 1.
"""

# Creating a dictionary to store the result of each Fibonacci number
fib_dict = {0: 0, 1: 1}

def fib(n: int) -> int:
    # If the number is in the dictionary return it 
    if n in fib_dict:
        return fib_dict[n]

    # If number is not in the dictionary, 
    # then calculate it and store it in the dictionary
    fib_dict[n] = fib(n - 1) + fib(n - 2)

    return fib_dict[n]