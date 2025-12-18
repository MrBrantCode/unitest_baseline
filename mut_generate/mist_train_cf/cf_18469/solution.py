"""
QUESTION:
Create a function `multiplication_table(n, m)` that prints a multiplication table of size n up to a maximum number m. The function should only include rows and columns up to the minimum of n and m. Both n and m must be positive integers. If either n or m is not a positive integer, the function should print an error message.
"""

def multiplication_table(n, m):
    """
    Prints a multiplication table of size n up to a maximum number m.

    Args:
        n (int): The size of the multiplication table.
        m (int): The maximum number in the multiplication table.

    Returns:
        None
    """

    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        print("n must be a positive integer.")
        return
    if not isinstance(m, int) or m <= 0:
        print("m must be a positive integer.")
        return
    if m > n:
        m = n
    
    # Create multiplication table
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(f"{i*j:3}", end=" ")  # Use string formatting to align numbers
        print()  # Print new line after each row