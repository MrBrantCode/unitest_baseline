"""
QUESTION:
Design a function named `min_rotations` that takes two parameters: `rotation_angle` and `target_angle`, and returns the minimum number of rotations of `rotation_angle` necessary to reach or exceed `target_angle` from the initial position on a circular path. The function should handle cases where `rotation_angle` does not evenly divide `target_angle`, and it should manage edge cases such as when `rotation_angle` is zero or when `target_angle` is the same as the initial position (zero).
"""

def min_rotations(rotation_angle, target_angle):
    if rotation_angle == 0:
        return "Rotation angle cannot be zero"
    if target_angle == 0:
        return 0
    return (target_angle + rotation_angle - 1) // rotation_angle