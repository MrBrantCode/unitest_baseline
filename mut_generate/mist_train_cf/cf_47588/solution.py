"""
QUESTION:
Create a function `fibonacci_program(n)` to calculate the nth Fibonacci number and return the sequence leading up to the nth term without using recursive function calls and with a time complexity less than O(n^2).
"""

def fibonacci_program(n):
    """
    Calculate the nth Fibonacci number and return the sequence leading up to the nth term.

    Args:
    n (int): The nth Fibonacci number to calculate.

    Returns:
    list: A list of Fibonacci numbers from 0 to the nth term.

    """
    # Initialize first two Fibonacci numbers
    Fibonacci_array=[0 , 1]
    
    # Add remaining numbers
    for i in range(2, n+1):
        Calculate_Next_Fibonacci = Fibonacci_array[i-1] +  Fibonacci_array[i-2]
        Fibonacci_array.append(Calculate_Next_Fibonacci)
    return Fibonacci_array