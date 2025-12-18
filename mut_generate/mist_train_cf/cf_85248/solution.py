"""
QUESTION:
Create a function called `fibonacci_sequence` that takes one parameter `maximum`. The function should use a while loop to generate and return all Fibonacci sequence numbers that are lesser than or equal to the given `maximum`. The Fibonacci sequence starts from 0 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def fibonacci_sequence(maximum):
    # Define the first two Fibonacci numbers
    num1, num2 = 0, 1

    # Start the while loop
    sequence = []
    while num1 <= maximum:
        # Append the current Fibonacci number
        sequence.append(num1)

        # Calculate the next Fibonacci number
        num1, num2 = num2, num1 + num2

    return sequence