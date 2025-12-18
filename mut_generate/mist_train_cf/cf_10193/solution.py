"""
QUESTION:
Create a function called `fibonacci_sequence` that takes one argument `num_elements` representing the number of elements in the Fibonacci sequence to generate. The function should return a list containing the Fibonacci sequence up to `num_elements` numbers, where the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def fibonacci_sequence(num_elements):
    # Initialize the list with the first two numbers of the sequence
    sequence = [0, 1]

    # Calculate the Fibonacci sequence
    for i in range(2, num_elements):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)

    return sequence