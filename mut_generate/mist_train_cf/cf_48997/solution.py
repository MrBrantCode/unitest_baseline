"""
QUESTION:
Implement a function `memory_allocation` that demonstrates the differences between stack and heap memory allocation in C++. Explain when to use each type of memory allocation, including the scenarios where one is preferred over the other due to their individual properties. Assume the function will be used to allocate memory for variables with temporary use within a function scope, as well as for large objects or arrays that need to be accessed globally.
"""

def memory_allocation(size):
    """
    This function demonstrates dynamic memory allocation for large objects or arrays.
    
    Args:
        size (int): The size of the array to be allocated.
    
    Returns:
        list: A list of specified size initialized with zeros.
    """
    return [0] * size