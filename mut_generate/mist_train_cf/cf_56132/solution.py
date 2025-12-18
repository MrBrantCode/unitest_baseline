"""
QUESTION:
Create a function `fib(n)` that calculates the nth term of the Fibonacci sequence and returns the entire sequence up to the nth term as a list, with a time complexity of O(N) and a space complexity of O(N). The function should also implement memoization to avoid redundant calculations. If the input `n` is less than 0, the function should return an error message.
"""

def fib(n):
    """
    Calculate the nth term of the Fibonacci sequence and return the entire sequence up to the nth term as a list.

    Args:
        n (int): The term in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to the nth term. If n is less than 0, returns an error message.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    # checks if the input is below 0 which is invalid.
    if n < 0:
        return "Invalid input. Please enter a positive number"

    # initializes a list to store the sequence
    fib_sequence = [0, 1] + [0] * (n - 1)

    # iterates from the 3rd term to nth term to fill the list
    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

    # returns the full fibonacci sequence list 
    return fib_sequence[:n+1]