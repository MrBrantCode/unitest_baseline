"""
QUESTION:
Create a function `print_multiplication_table(size)` that prints a multiplication table of the given size. The size must be an odd number between 3 and 11, inclusive. The function should generate the table using nested loops without using any built-in multiplication functions or operators. The time complexity of the function should be O(n^2), where n is the given size of the multiplication table.
"""

def print_multiplication_table(size):
    if size % 2 == 0 or size < 3 or size > 11:
        print("Invalid size! Size should be an odd number between 3 and 11, inclusive.")
        return
    
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            result = 0
            for k in range(i):
                result += j
            print(result, end="\t")
        print()