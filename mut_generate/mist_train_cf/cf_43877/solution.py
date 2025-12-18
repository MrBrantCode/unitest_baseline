"""
QUESTION:
Create a function `calculate_median` that takes a list of real numbers as input and returns the median value of the dataset. The input list can contain integers and/or floats and must be non-empty. The function should calculate the median by first sorting the data in ascending order, then finding the middle value(s) based on whether the number of elements is odd or even.
"""

def calculate_median(data):
    # Step 1: Sort the data
    data.sort()
    
    # Step 2: Find the middle value
    n = len(data)
    index = n // 2
    
    # Check if the number of data points is odd
    if n % 2:
        return data[index]
    else:
        return (data[index - 1] + data[index]) / 2