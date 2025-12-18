"""
QUESTION:
Create a Python program with a `main` function that calculates and displays the area and perimeter of a rectangle based on user input. The program should use separate functions to calculate the area and perimeter. The program should validate user inputs to ensure they are positive integers greater than 0 and less than or equal to 100, and handle any potential exceptions that may occur during user input or calculation.
"""

def main(length, width):
    def calculate_area(length, width):
        return length * width

    def calculate_perimeter(length, width):
        return 2 * (length + width)

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    return area, perimeter