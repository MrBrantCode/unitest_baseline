"""
QUESTION:
Write a function `print_multiplication_table` that prints the result of a multiplication table of a given size. The table size must be at least 10x10 and at most 20x20.
"""

def print_multiplication_table(table_size):
    if table_size < 10 or table_size > 20:
        print("Table size must be between 10 and 20")
        return
    
    for i in range(1, table_size + 1):
        for j in range(1, table_size + 1):
            print(f"{i} * {j} = {i * j}")
        print()