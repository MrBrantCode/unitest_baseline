"""
QUESTION:
Create a function `rectangle_area` that calculates the area of a rectangle given its length and width. The function should ensure that both length and width are numbers. If either input is not a number, the function should prompt the user to input a valid number until a valid number is entered.
"""

def rectangle_area(length, width):
    while not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        try:
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    area = length * width
    return area