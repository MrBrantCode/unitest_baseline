"""
QUESTION:
Write a function named `print_multiplication_table` that takes two parameters, `start` and `end`, representing the range of numbers for which to print the multiplication table. The function should handle cases where `start` or `end` are not positive integers, printing an error message and returning without printing the table. The multiplication table should include the numbers from 1 to 10, and each row should be printed on a separate line with the numbers aligned properly.
"""

def print_multiplication_table(start, end):
    if start < 0 or end < 0 or not isinstance(start, int) or not isinstance(end, int):
        print("Invalid range. Please enter positive integer values.")
        return
    
    for i in range(start, end + 1):
        for j in range(1, 11):
            print("{:4}".format(i * j), end="")
        print()