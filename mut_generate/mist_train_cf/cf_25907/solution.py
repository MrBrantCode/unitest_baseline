"""
QUESTION:
Write a function named `calculate_total_distance` that takes initial velocity and acceleration as input and returns the total distance traveled. The function should assume that the object's initial position is 0 and it moves for 9 seconds.
"""

def calculate_total_distance(initial_velocity, acceleration):
    time = 9  # assuming the object moves for 9 seconds
    total_distance = (initial_velocity * time) + 0.5 * acceleration * (time ** 2)
    return total_distance