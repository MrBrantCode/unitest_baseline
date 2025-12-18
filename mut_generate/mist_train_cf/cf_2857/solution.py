"""
QUESTION:
Write a function `calculate_surface_area` that takes in four integers `n`, `m`, `k`, and `c`, representing the length, width, height, and number of unique colors of a rectangular prism, respectively, and returns an integer representing the total surface area of the prism. Each face of the prism must have a different color, and the colors are chosen from a set of `c` colors. The values of `n`, `m`, `k`, and `c` are within the range of 1 to 1000. The function should have a time complexity of O(1) and a space complexity of O(1), and it should not use any built-in functions or libraries that perform arithmetic operations, only using bitwise operators and basic logical operations.
"""

def calculate_surface_area(n, m, k, c):
    face_area = 2 * (n * m + m * k + k * n)
    total_area = face_area * c
    return total_area