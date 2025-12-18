"""
QUESTION:
Write a function `print_multiplication_table(n, m)` that prints a multiplication table of size n up to a maximum number m, minimizing the number of multiplication operations. The function should take two parameters: `n` and `m`, both of which are positive integers. If `m` is greater than `n`, the function should print only the necessary rows. The function should validate the input parameters and print "Invalid input" if the inputs are not valid.
"""

def print_multiplication_table(n, m):
    """
    Prints a multiplication table of size n up to a maximum number m, 
    minimizing the number of multiplication operations.

    Args:
        n (int): The size of the multiplication table.
        m (int): The maximum number in the multiplication table.

    Returns:
        None
    """
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0 or m > n:
        print("Invalid input")
        return
    
    for i in range(1, m + 1):
        row = []
        for j in range(1, n + 1):
            if j <= i:
                row.append(str(i * j))
            else:
                row.append('')
        print('\t'.join(row))