"""
QUESTION:
Create a function `create_array` that takes the number of rows and columns as input, and returns a 2D array. The function should prompt the user to input an integer for each index in the array, and keep asking until a valid integer is entered.
"""

def create_array(rows, cols):
    arr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    num = int(input(f"Enter an integer for index [{i}][{j}]: "))
                    row.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        arr.append(row)
    return arr