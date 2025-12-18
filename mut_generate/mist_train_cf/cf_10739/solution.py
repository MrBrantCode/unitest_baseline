"""
QUESTION:
Create a function named `print_triangle_pattern(rows)` that takes an integer `rows` as input and prints a triangle pattern. The number of rows should be between 5 and 10 (inclusive). The triangle pattern should consist of numbers in ascending order followed by numbers in descending order on each row, with the first row having only one number, the second row having three numbers, and so on.
"""

def print_triangle_pattern(rows):
    # Check if the number of rows is within the specified range
    if rows < 5 or rows > 10:
        print("Number of rows should be between 5 and 10 (inclusive).")
        return
    
    for i in range(1, rows+1):
        # Print spaces in the beginning of each row
        print(" " * (rows-i), end="")
        
        # Print numbers in ascending order
        for j in range(1, i+1):
            print(j, end="")
        
        # Print numbers in descending order
        for k in range(i-1, 0, -1):
            print(k, end="")
        
        print()  # Move to the next line after each row