"""
QUESTION:
Create a function `create_array(rows, columns)` that takes the number of rows and columns as input, prompts the user to enter values for each element in the array, and returns a 2D array with the user-input values. The function should validate user input to ensure it is a valid integer.
"""

def create_array(rows, columns):
    array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            valid_input = False
            while not valid_input:
                try:
                    num = int(input(f"Enter the value for element ({i}, {j}): "))
                    row.append(num)
                    valid_input = True
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")

        array.append(row)
    return array