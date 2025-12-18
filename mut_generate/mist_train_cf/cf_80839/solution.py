"""
QUESTION:
Write a function named `calculate_median` that takes a list of numbers as input, calculates the median of the list, and returns the result. The function should handle both odd and even length lists by returning the middle value for odd lengths and the average of the two middle values for even lengths.
"""

def calculate_median(data):
    data.sort()
    n = len(data)
    
    if n % 2 == 1:
        # For an odd length list, the median is the middle value
        return data[n // 2]
    else:
        # For an even length list, the median is the average of the two middle values
        return (data[n // 2 - 1] + data[n // 2]) / 2