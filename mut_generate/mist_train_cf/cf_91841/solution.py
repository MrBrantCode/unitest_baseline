"""
QUESTION:
Write a Python function `print_multiplication_table(n, m)` to print a multiplication table of a given size n and maximum number m. The function should handle cases where m is greater than n and validate that n and m are positive integers, with m not greater than 10. The table should be printed in a visually appealing format with proper spacing and alignment.
"""

def print_multiplication_table(n, m):
    # Validate input parameters
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0 or m > 10:
        print("Invalid input parameters")
        return
    
    # Determine the number of rows and columns in the table
    rows = min(n, m)
    cols = min(n, m)

    # Print the table
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if j <= i:
                # Calculate the product and print it with proper spacing and alignment
                product = i * j
                print("{:4d}".format(product), end='')
        print()