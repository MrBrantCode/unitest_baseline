"""
QUESTION:
Create a function called `create_array` that takes two parameters: `rows` and `columns`, representing the dimensions of a 2D array. The function should prompt the user to input integers for each element of the array, validate the input to ensure it's a non-negative integer, and store the validated input in the array. If the input is invalid (non-integer or negative), display an error message and ask for input again until a valid non-negative integer is entered. The function should return the populated 2D array. Additionally, the number of rows and columns should also be validated to be positive integers before calling the `create_array` function.
"""

def create_array(rows, columns):
    arr = []
    for i in range(rows):
        row = []
        for j in range(columns):
            valid_input = False
            while not valid_input:
                value = input("Enter an integer: ")
                if not value.isdigit():
                    print("Error: Invalid input. Please enter an integer.")
                elif int(value) < 0:
                    print("Error: Negative integer entered. Please enter a non-negative integer.")
                else:
                    row.append(int(value))
                    valid_input = True
        arr.append(row)
    return arr