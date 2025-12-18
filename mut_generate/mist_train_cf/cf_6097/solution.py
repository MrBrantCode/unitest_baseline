"""
QUESTION:
Write a function named `classify_coordinates` to classify a given set of X and Y coordinates into four categories: 
1. Positive X and Positive Y
2. Positive X and Negative Y
3. Negative X and Positive Y
4. Negative X and Negative Y

The input coordinates should be in the range of -1000 to 1000. The function should handle outliers (coordinates outside the range of -1000 to 1000) and missing values by classifying them as separate categories.
"""

def classify_coordinates(x, y):
    """
    Classify a given set of X and Y coordinates into four categories:
    1. Positive X and Positive Y
    2. Positive X and Negative Y
    3. Negative X and Positive Y
    4. Negative X and Negative Y

    Args:
        x (int): The X coordinate
        y (int): The Y coordinate

    Returns:
        str: The classification of the coordinates
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Invalid input type"
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return "Outlier"
    if x > 0 and y > 0:
        return "Positive X and Positive Y"
    elif x > 0 and y < 0:
        return "Positive X and Negative Y"
    elif x < 0 and y > 0:
        return "Negative X and Positive Y"
    elif x < 0 and y < 0:
        return "Negative X and Negative Y"
    else:
        return "Missing value"