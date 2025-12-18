"""
QUESTION:
Design a function named `print_mult_table` that takes an integer `n` as input and prints the multiplication table up to `n`. The function should also print the sum and average of each row. If `n` is less than or equal to 0, the function should print "Enter a positive number!" and not print any multiplication table.
"""

def print_mult_table(n):
    if n <= 0:
        print("Enter a positive number!")
        return
    for i in range(1, n+1):
        sum_row = 0
        for j in range(1, n+1):
            val = i*j
            print(val, end=" ")
            sum_row += val
        print("Sum:", sum_row, "Average:", sum_row/n)
    return