"""
QUESTION:
Create a function called `latest_version` that takes a list of version numbers as input, where each version number is a string in the format "x.y.z" and x, y, and z are non-negative integers. The function should return the latest version number as a string. The version numbers should be compared based on their numerical values.
"""

def latest_version(versions):
    return max(versions, key=lambda x: list(map(int, x.split('.'))))