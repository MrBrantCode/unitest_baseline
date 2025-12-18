"""
QUESTION:
Create a function called "print_multiplication_table" that takes two integer parameters "x" and "y" and prints the multiplication table for the range of integers from "x" to "y". The function should only accept positive integers and "x" must be less than or equal to "y".
"""

def print_multiplication_table(x, y):
    # Check if x and y are positive numbers
    if x <= 0 or y <= 0:
        print("Error: x and y must be positive numbers.")
        return

    # Check if x is less than or equal to y
    if x > y:
        print("Error: x must be less than or equal to y.")
        return

    # Iterate from x to y
    for i in range(x, y+1):
        # Print i followed by a colon
        print(str(i) + ":", end=" ")
        
        # Iterate from x to y
        for j in range(x, y+1):
            # Calculate the product of i and j
            product = i * j
            # Print the product followed by a tab character
            print(str(product) + "\t", end="")

        # Print a new line character
        print()