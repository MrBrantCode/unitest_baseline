"""
QUESTION:
Implement a Python class named `Surface` with a method `calculate_area()`. The `Surface` class should have an initializer that takes a parameter `M`, a list of lists representing the dimensions of a 3D object's faces. Each inner list represents a face of the object, and the elements of the inner list represent the lengths of the sides of the face. The `calculate_area()` method should return the total surface area of the 3D object, calculated by summing the areas of its faces.
"""

def surface_area(M):
    total_area = 0
    for face in M:
        area = 0
        for i in range(len(face)):
            next_index = (i + 1) % len(face)
            area += face[i] * face[next_index]
        total_area += area
    return total_area