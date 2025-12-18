"""
QUESTION:
Implement a function named `perform_operation` that takes in two parameters: a list of shape objects and a string indicating the operation to be performed on the shapes. The function should use polymorphism to handle different types of shapes and perform the requested operation.

The function should support the following operations: 
1. "calculate total area"
2. "calculate perimeter"
3. "count number of triangles"
4. "count number of circles"
5. "find shape with maximum area"
6. "calculate average area"

Constraints:
- The list of shapes can contain up to 1000 shapes.
- Each shape object should contain at least three attributes: "type", "area", and "perimeter".
- The "type" attribute of each shape should be a string.
- The "area" attribute of each shape should be a non-negative float.
- The "perimeter" attribute of each shape should be a non-negative float.
- The "type" attribute can only be one of the following: "triangle", "rectangle", "circle", "square", "pentagon".
- The function should return appropriate error messages for invalid inputs or unsupported operations.
"""

def perform_operation(shapes, operation):
    if operation == "calculate total area":
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        return total_area
    elif operation == "calculate perimeter":
        total_perimeter = 0
        for shape in shapes:
            total_perimeter += shape.calculate_perimeter()
        return total_perimeter
    elif operation == "count number of triangles":
        count = 0
        for shape in shapes:
            if shape.shape_type == "triangle":
                count += 1
        return count
    elif operation == "count number of circles":
        count = 0
        for shape in shapes:
            if shape.shape_type == "circle":
                count += 1
        return count
    elif operation == "find shape with maximum area":
        max_area_shape = None
        max_area = 0
        for shape in shapes:
            area = shape.calculate_area()
            if area > max_area:
                max_area = area
                max_area_shape = shape
        return max_area_shape
    elif operation == "calculate average area":
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        average_area = total_area / len(shapes)
        return average_area
    else:
        return "Unsupported operation"