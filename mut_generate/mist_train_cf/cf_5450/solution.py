"""
QUESTION:
Implement a function named `detect_outliers` that takes an array of integers as input and returns a list of outliers in the array. The input array should have at least 100 elements. An outlier is defined as a value that is either greater than 5 times the interquartile range (IQR) above the third quartile or less than 5 times the IQR below the first quartile. The function should have a time complexity of O(n) and should not use any built-in functions or libraries to calculate the quartiles or interquartile range.
"""

def detect_outliers(array):
    n = len(array)
    
    # Sort the array in ascending order
    array.sort()
    
    # Calculate the index of the first quartile (Q1) and third quartile (Q3)
    q1_index = int(n * 0.25)
    q3_index = int(n * 0.75)
    
    # Calculate the first quartile (Q1)
    q1 = (array[q1_index] + array[q1_index + 1]) / 2 if n % 4 == 0 else array[q1_index]
    
    # Calculate the third quartile (Q3)
    q3 = (array[q3_index] + array[q3_index + 1]) / 2 if n % 4 == 0 else array[q3_index]
    
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    
    # Define the lower and upper thresholds for outliers
    lower_threshold = q1 - 5 * iqr
    upper_threshold = q3 + 5 * iqr
    
    # Detect outliers in the array
    outliers = []
    for value in array:
        if value < lower_threshold or value > upper_threshold:
            outliers.append(value)
    
    return outliers