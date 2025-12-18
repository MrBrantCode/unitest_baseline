"""
QUESTION:
Create a function `print_multiplication_table(size)` that prints a multiplication table of a given size. The size must be an odd number between 5 and 15, inclusive. The function should use nested loops and bitwise operations to generate the table without using any built-in multiplication functions or operators, and its time complexity should be O(n^2), where n is the given size.
"""

def print_multiplication_table(size):
    if size % 2 == 0 or size < 5 or size > 15:
        print("Invalid size. Please enter an odd number between 5 and 15.")
        return

    for i in range(1, size+1):
        for j in range(1, size+1):
            product = 0
            for k in range(j.bit_length()):  
                if j & (1 << k):  
                    product += i << k  
            print(product, end="\t")
        print()