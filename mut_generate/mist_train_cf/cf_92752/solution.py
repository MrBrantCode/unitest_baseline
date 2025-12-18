"""
QUESTION:
Implement a function named `perform_operation` that takes in two parameters: a list of shapes and a string indicating the operation to be performed on the shapes. The function should use polymorphism to handle different types of shapes and perform the requested operation accordingly. The function should support at least two operations: "calculate total area" and "count number of rectangles". The function should return the result of the operation.
"""

def perform_operation(shapes, operation):
    if operation == "calculate total area":
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        return total_area

    elif operation == "count number of rectangles":
        rectangle_count = 0
        for shape in shapes:
            if shape.type == "Rectangle":
                rectangle_count += 1
        return rectangle_count

    else:
        return "Invalid operation"