"""
QUESTION:
Increment the Counter by 20 without Addition or Multiplication

Write a function called 'increment_counter' that increments a given counter by 20 without using the addition operator (+) or multiplication operator (*). 

The function should take one argument, the initial counter value, and return the incremented value.
"""

def increment_counter(counter):
    """
    Increments a given counter by 20 without using the addition operator (+) or multiplication operator (*).
    
    Args:
        counter (int): The initial counter value.
    
    Returns:
        int: The incremented value.
    """
    return counter | (16 | 4)