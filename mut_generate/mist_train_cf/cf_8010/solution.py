"""
QUESTION:
Write a function named `generate_fibonacci_sequence(n)` that generates a Fibonacci sequence up to the nth number. The function should return an error message for negative inputs. The time complexity should be O(n) and the space complexity should be O(1), excluding the space required for the output sequence.
"""

def generate_fibonacci_sequence(n):
    """
    Generates a Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of Fibonacci numbers up to the nth number, or an error message if n is negative.
    """

    # Check if n is less than 0 and return an error message if it is
    if n < 0:
        return "Invalid input! Please enter a positive number."

    # Handle special cases when n is 0, 1, or 2
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the Fibonacci sequence with the first two numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence iteratively using a loop
    for i in range(2, n):
        # Calculate the next Fibonacci number as the sum of the previous two numbers
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        # Append the next Fibonacci number to the sequence
        fib_sequence.append(next_fib)

    return fib_sequence