"""
QUESTION:
Create a function called `fibonacci_sequence` that takes the number of elements as an argument and returns a list containing the Fibonacci sequence up to that number. The number of elements must be between 2 and 30 (inclusive). The function should not use recursion.
"""

def fibonacci_sequence(num_elements):
    if num_elements < 2 or num_elements > 30:
        return "Invalid input. Number of elements must be between 2 and 30 (inclusive)."
    
    sequence = [0, 1]
    
    for i in range(2, num_elements):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence