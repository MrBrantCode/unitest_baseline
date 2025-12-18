"""
QUESTION:
Calculate the total surface area of a rectangular prism with length n cm, width m cm, and height k cm, where each face has a different color chosen from c colors. Write a function `calculate_surface_area` that takes four integers n, m, k, and c as input, with the restrictions that 1 <= n, m, k, c <= 1000. The function should return an integer representing the total surface area of the prism. The solution must have a time complexity of O(1) and a space complexity of O(1), and can only use bitwise operators and basic logical operations.
"""

def calculate_surface_area(n, m, k, c):
    return 2 * (n * m + m * k + k * n) * c