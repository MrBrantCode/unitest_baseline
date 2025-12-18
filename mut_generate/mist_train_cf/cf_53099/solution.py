"""
QUESTION:
Create a function `getSubMaximum` that takes a 2D list `b` as input and returns the penultimate maximum data point. The function should handle cases where the 2D list or any of its sub-lists might be empty, and should return `None` if there are not enough elements to find the second maximum. The time complexity should be O(n^2) and the space complexity should be O(1).
"""

def getSubMaximum(b):
    # Initialize the maximum and second maximum to None
    max1 = max2 = None

    for sublist in b:
        for num in sublist:
            # If this number is greater than the current maximum, update the maximum and second maximum
            if max1 is None or num > max1:
                max2 = max1
                max1 = num
            # If this number is not the maximum but is greater than the second maximum, update the second maximum
            elif max1 != num and (max2 is None or num > max2):
                max2 = num

    return max2