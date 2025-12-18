"""
QUESTION:
Write a function `transitive_closure_less_than` that calculates the transitive closure of the binary relation "less than or equal to" on a given set of integers. The function should return a set of all pairs (a, b) such that a is less than or equal to b, and there is a sequence of intermediate integers that connects a to b. The input will be a list of distinct integers.
"""

def transitive_closure_less_than(numbers):
    """
    This function calculates the transitive closure of the binary relation "less than or equal to" on a given set of integers.
    
    Args:
        numbers (list): A list of distinct integers.
    
    Returns:
        set: A set of all pairs (a, b) such that a is less than or equal to b, and there is a sequence of intermediate integers that connects a to b.
    """
    closure_set = set()
    
    # Generate all possible pairs of integers
    for a in numbers:
        for b in numbers:
            # Check if a is less than or equal to b
            if a <= b:
                # Add the pair to the closure set
                closure_set.add((a, b))
    
    return closure_set