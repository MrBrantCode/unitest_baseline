"""
QUESTION:
Create a function `operation_on_sets` that performs a specified set operation (union, intersection, difference, or Cartesian product) on two input sets. The function should take three parameters: two sets and the operation to be performed. It should return the result of the operation and handle invalid inputs and unforeseen issues by catching exceptions and returning an error message.
"""

def operation_on_sets(set1, set2, operation):
    """
    This function performs the specified operation on the provided sets.

    Parameters:
    set1: The first set.
    set2: The second set.
    operation: The operation to perform. Can be 'union', 'intersection', 'difference', or 'product'.

    Returns:
    The result of performing the operation on the sets.
    """
    try:
        set1 = set(set1)
        set2 = set(set2)

        if operation == 'union':
            return set1.union(set2)
        elif operation == 'intersection':
            return set1.intersection(set2)
        elif operation == 'difference':
            return set1.difference(set2)
        elif operation == 'product':
            return set((a, b) for a in set1 for b in set2)
        else:
            return "Invalid operation"
    except Exception as e:
        return f"An error occurred: {e}"