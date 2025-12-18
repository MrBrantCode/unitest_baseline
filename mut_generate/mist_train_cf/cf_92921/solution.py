"""
QUESTION:
Create a function `print_odd_multiplication_table(n)` that takes a single integer `n` as an argument and prints out the corresponding multiplication table, displaying only the odd numbers. If the input is not a positive integer, the function should display an error message "Error: Input must be a positive integer".
"""

def print_odd_multiplication_table(n):
    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        print("Error: Input must be a positive integer")
        return

    # Print the multiplication table
    for i in range(1, n+1):
        for j in range(1, n+1):
            result = i * j
            if result % 2 != 0:
                print(result, end="\t")
            else:
                print("-", end="\t")
        print()