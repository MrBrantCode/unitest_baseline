"""
QUESTION:
Write a function called "calculate_distance" that takes in two 3D points as input and returns the square root of the sum of the squares of the differences in each coordinate. The function should not use the standard distance formula, any mathematical functions or libraries, and should have a time complexity of O(1).
"""

def calculate_distance(point1, point2):
    distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2) ** 0.5
    return distance