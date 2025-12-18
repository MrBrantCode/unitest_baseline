"""
QUESTION:
Write a function `euclidean_distance` that calculates the Euclidean Distance in n-dimensional space. The function should take two lists of numbers `point1` and `point2` representing points in n-dimensional space, and return the Euclidean distance between them. The function must not use any external or built-in math libraries. The function should also check if the two input lists have the same number of dimensions, and return an error message if they do not.
"""

def entance(point1, point2):
    if len(point1) != len(point2):
        return "Error: Points must have the same number of dimensions"
        
    return sum((point1[i] - point2[i]) ** 2 for i in range(len(point1))) ** 0.5