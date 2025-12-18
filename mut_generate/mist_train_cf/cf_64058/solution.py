"""
QUESTION:
Write a function named 'calculate_time_complexity' with a single input 'n', where 'n' is the number of iterations for the outer loop, to calculate the Big O notation complexity of the given iterative algorithm. The algorithm consists of two nested loops where the outer loop runs 'n' times and the inner loop runs 'i' times, with 'i' being the current iteration of the outer loop, and a constant time complexity operation inside the inner loop. Assume all operations, including addition and array referencing, have a constant time complexity of O(1).
"""

def calculate_time_complexity(n):
    """
    This function calculates the time complexity of an iterative algorithm.
    
    The algorithm consists of two nested loops where the outer loop runs 'n' times 
    and the inner loop runs 'i' times, with 'i' being the current iteration of the 
    outer loop, and a constant time complexity operation inside the inner loop.
    
    Parameters:
    n (int): The number of iterations for the outer loop.
    
    Returns:
    str: The time complexity of the algorithm in Big O notation.
    """
    # The time complexity of the algorithm is O(n^2)
    return "O(n^2)"