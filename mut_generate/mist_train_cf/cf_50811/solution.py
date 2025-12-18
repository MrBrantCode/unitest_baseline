"""
QUESTION:
Design a function named `exponentiate_tuples` that takes two tuples of the same size as input, each containing real numbers. The function should return a new tuple containing the result of an element-wise exponentiation operation, where the corresponding elements of the first tuple are raised to the power of the corresponding elements of the second tuple. If the second tuple contains any negative values, or if the tuples are not of equal size, or if the inputs are not tuples, or if the tuple elements are not real numbers, the function should return an error message.
"""

def exponentiate_tuples(t1, t2):
    # Check if inputs are tuples
    if not isinstance(t1, tuple) or not isinstance(t2, tuple):
        return "Error: Input is not a tuple!"
        
    # Check if size of inputs are equal
    if len(t1) != len(t2):
        return "Error: Tuples are of different sizes!"
        
    try:
        # Try to convert elements to floats
        t1 = tuple(map(float, t1))
        t2 = tuple(map(float, t2))
    except:
        return "Error: Tuple elements are not real numbers!"
        
    # Check if second tuple contains any negative value
    if any(ele < 0 for ele in t2):
        return "Error: Second Tuple contains negative values!"
        
    # Perform element-wise exponentiation and return the new tuple
    return tuple(map(pow, t1, t2))