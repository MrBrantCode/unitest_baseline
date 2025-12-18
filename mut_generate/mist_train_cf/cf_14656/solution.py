"""
QUESTION:
Create a function called "print_multiplication_table" that takes two parameters: a positive integer "x" and a positive integer "n". The function should print the multiplication table for "x" up to the limit "n". If either "x" or "n" is not a positive number, the function should print an error message and return.
"""

def print_multiplication_table(x, n):
    if x <= 0:
        print("Error: x must be a positive number")
        return
    
    if n <= 0:
        print("Error: n must be a positive number")
        return
    
    for i in range(1, n+1):
        print(str(i) + ":", end="")
        for j in range(1, x+1):
            product = i * j
            print(str(product) + "\t", end="")
        print()