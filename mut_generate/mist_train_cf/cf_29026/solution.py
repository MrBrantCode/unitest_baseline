"""
QUESTION:
Given a set of points and a threshold value, determine whether the shape formed by the points is "squarish". A shape is considered "squarish" if the following conditions are met: 
1. All side lengths are approximately the same, with the ratio of the shortest to the longest side length being greater than or equal to the given threshold.
2. All angles are approximately the same, with a difference of less than 0.1 radians between each angle and the first angle.

Implement the `squarish` function, which takes in the points and a threshold value, and returns `True` if the shape formed by the points is "squarish" based on the conditions mentioned above, and `False` otherwise.

Function Signature: 
```python
def squarish(points, threshold=.6) -> bool:
```
"""

import math

def squarish(points, threshold=.6) -> bool:
    """
    This function determines whether the shape formed by the given points is "squarish".
    
    A shape is considered "squarish" if the following conditions are met:
    1. All side lengths are approximately the same, with the ratio of the shortest to the longest side length being greater than or equal to the given threshold.
    2. All angles are approximately the same, with a difference of less than 0.1 radians between each angle and the first angle.
    
    Args:
    points (list): A list of tuples representing the points in the shape.
    threshold (float): The minimum ratio of the shortest to the longest side length. Defaults to 0.6.
    
    Returns:
    bool: True if the shape is "squarish", False otherwise.
    """

    # Calculate the distances between consecutive points
    distances = [math.sqrt((points[i][0] - points[i+1][0])**2 + (points[i][1] - points[i+1][1])**2) for i in range(len(points)-1)]
    
    # Calculate the angles between consecutive points
    angles = []
    for i in range(len(points)):
        p1 = points[i-1]
        p2 = points[i]
        p3 = points[(i+1) % len(points)]
        v1 = (p1[0] - p2[0], p1[1] - p2[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])
        dot_product = v1[0]*v2[0] + v1[1]*v2[1]
        mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
        mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
        angle = math.acos(dot_product / (mag_v1 * mag_v2))
        angles.append(angle)
    
    # Check if the distances and angles meet the conditions
    shortest = float(min(distances))
    longest = float(max(distances))
    distance_ratio = shortest / longest
    distances_are_close_enough = distance_ratio >= threshold
    angles_are_close_enough = all(abs(a - angles[0]) < 0.1 for a in angles)
    
    return distances_are_close_enough and angles_are_close_enough