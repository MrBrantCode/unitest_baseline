"""
QUESTION:
Create a function called `square_evens` that takes a list of integers as input and returns a list of squares of even numbers from the input list. Implement this function using a while loop and include exception handling to catch any potential errors.
"""

def square_evens(numbers):
    """
    This function takes a list of integers as input and returns a list of squares of even numbers from the input list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of squares of even numbers from the input list.
    """
    squared_evens = []
    i = 0
    try:
        while i < len(numbers):
            squared = numbers[i]**2
            if squared % 2 == 0:
                squared_evens.append(squared)
            i += 1
    except Exception as e:
        print("Error occurred:", e)
    return squared_evens