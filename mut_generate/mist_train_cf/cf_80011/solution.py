"""
QUESTION:
visiblePoints(points, angle, location)

You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] denote integral coordinates on the X-Y plane. Return the minimum number of points you can see. 

Constraints: 1 <= points.length <= 105, points[i].length == 2, location.length == 2, 0 <= angle < 360, 0 <= posx, posy, xi, yi <= 100.
"""

import math

def visiblePoints(points, angle, location):
    """
    This function calculates the minimum number of visible points given an array of points, 
    a viewing angle, and a location.

    Args:
    points (list): A list of points, where each point is a list of two integers.
    angle (int): The viewing angle in degrees.
    location (list): The location as a list of two integers.

    Returns:
    int: The minimum number of visible points.
    """

    # Calculate the angle in radians
    angle_rad = math.pi * angle / 180

    # Initialize variables to store the angles and count of points at the same location
    angles = []
    same_location = 0

    # Iterate over each point
    for point in points:
        # If the point is at the same location, increment the count
        if point == location:
            same_location += 1
        else:
            # Calculate the angle of the point relative to the location
            dx, dy = point[0] - location[0], point[1] - location[1]
            angle_point = math.atan2(dy, dx)

            # Since we may rotate counterclockwise, and the angles are recorded clockwise, multiply by -1
            angles.append(-angle_point)

    # If there are no points other than the location, return the count of points at the location
    if not angles:
        return same_location

    # Sort the angles
    angles.sort()

    # Initialize variables to store the maximum count and the left pointer
    max_count = 0
    left = 0

    # Iterate over the sorted angles
    for right in range(len(angles)):
        # While the difference between the current angle and the angle at the left pointer is greater than the viewing angle
        while angles[right] - angles[left] > angle_rad:
            # Move the left pointer to the right
            left += 1

        # Update the maximum count
        max_count = max(max_count, right - left + 1)

    # Return the maximum count plus the count of points at the same location
    return max_count + same_location