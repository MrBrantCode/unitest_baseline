"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns a list of the first `n` numbers in the Fibonacci sequence. The function must have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output list. If `n` is less than or equal to 0, the function should return an empty list.
"""

def fibonacci(n):
    if n <= 0:
        return []
    
    # Variables to store the current and previous numbers
    current = 1
    previous = 0
    
    # List to store the Fibonacci sequence
    sequence = [previous, current]
    
    # Calculate the Fibonacci sequence up to the n-th number
    for _ in range(2, n):
        next_num = current + previous
        sequence.append(next_num)
        
        # Update the current and previous numbers
        previous = current
        current = next_num
    
    return sequence