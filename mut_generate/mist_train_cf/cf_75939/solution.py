"""
QUESTION:
Write a function called `calculate_unique_examples` that takes in a list of integers representing the number of possible values for each variable and an integer representing the number of possible class values. The function should return the maximum possible number of unique examples that can be generated. Assume that the number of possible values for each variable and the class are finite and non-negative.
"""

def calculate_unique_examples(variables, classes):
    """
    Calculate the maximum possible number of unique examples that can be generated.
    
    Args:
    variables (list): A list of integers representing the number of possible values for each variable.
    classes (int): An integer representing the number of possible class values.
    
    Returns:
    int: The maximum possible number of unique examples.
    """
    # Calculate the maximum number of unique examples by multiplying the number of possible values of each variable and the class
    return classes * eval('*'.join(map(str, variables)))