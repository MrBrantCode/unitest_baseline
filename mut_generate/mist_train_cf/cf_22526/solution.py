"""
QUESTION:
Create a function called "isImmutable" that takes in a list and a function as parameters. The function should check if the provided function is pure and immutable by ensuring that it doesn't modify the original list and always produces the same output given the same input.
"""

def isImmutable(input_list, func):
    """
    Checks if a given function is pure and immutable.
    
    Args:
    input_list (list): The input list to be used for the function.
    func (function): The function to be checked for purity and immutability.
    
    Returns:
    bool: True if the function is pure and immutable, False otherwise.
    """
    
    # Create a copy of the input list to check for immutability
    original_list = input_list[:]
    
    # Apply the function to the input list
    func(input_list)
    
    # Check if the original list has been modified
    if input_list != original_list:
        return False
    
    # Check for purity by applying the function multiple times with the same input
    result1 = func(input_list)
    result2 = func(input_list)
    
    # If the results are different, the function is not pure
    if result1 != result2:
        return False
    
    return True