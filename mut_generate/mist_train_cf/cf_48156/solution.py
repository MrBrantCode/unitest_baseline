"""
QUESTION:
Create a function named `bitwise_operations` that takes four arguments (a, b, c, d) and returns the result of performing three different bitwise operations between them. The operations should be performed in the following sequence: operation 1 between a and b, operation 2 between the result of operation 1 and c, operation 3 between the result of operation 2 and d. The operations should combine at least three different bitwise operators. The function should also handle potential exceptions and print an error message if an illegal operation was attempted.
"""

def bitwise_operations(a=1, b=2, c=3, d=4):
    """
    Perform three different bitwise operations between four numbers.
    
    The operations are performed in the following sequence: 
    operation 1 (AND) between a and b, 
    operation 2 (OR) between the result of operation 1 and c, 
    operation 3 (XOR) between the result of operation 2 and d.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.
        d (int): The fourth number.
    
    Returns:
        int: The result of the bitwise operations.
    
    Raises:
        Exception: If an error occurs during the operation.
    """
    try:
        result = a & b
        result = result | c
        result = result ^ d
        return result
    except Exception as e:
        print(f"An error occurred: {e}")