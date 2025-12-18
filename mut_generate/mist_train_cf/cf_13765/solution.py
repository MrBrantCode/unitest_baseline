"""
QUESTION:
Write a function called `fibonacci` that calculates the Fibonacci sequence up to the n-th number, where n is provided as an argument. The function must have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output. The function should return a list of the Fibonacci sequence up to the n-th number, with the first two numbers being 0 and 1.
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