"""
QUESTION:
Create a function called `increment_version` that takes a string representing a version number in the format "x.y.z" as input, where x, y, and z are non-negative integers. The function should increment the version number by incrementing the z value by 1. If z reaches 10, it should reset to 0 and both y and z should be incremented accordingly. If y reaches 10, it should reset to 0 and x should be incremented accordingly. The function should return the incremented version number as a string.
"""

def increment_version(version):
    x, y, z = map(int, version.split('.'))
    
    if z < 9:
        z += 1
    elif z == 9:
        z = 0
        if y < 9:
            y += 1
        elif y == 9:
            y = 0
            x += 1
    
    return f"{x}.{y}.{z}"