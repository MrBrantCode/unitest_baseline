"""
QUESTION:
Create a function `calculate_statistics(numbers)` that takes a list of numbers as input and returns the maximum, minimum, and average of the numbers in the list, excluding any outliers. The function should consider a number as an outlier if it is outside 1.5 times the interquartile range from the lower and upper quartiles. The list may contain duplicates and negative numbers.
"""

def calculate_statistics(numbers):
    # Sort the list in ascending order
    numbers.sort()
    
    # Calculate the lower and upper quartiles
    n = len(numbers)
    lower_quartile = numbers[n//4]
    upper_quartile = numbers[(3*n)//4]
    
    # Calculate the interquartile range
    iqr = upper_quartile - lower_quartile
    
    # Remove any outliers outside 1.5 times the interquartile range from the quartiles
    numbers = [num for num in numbers if lower_quartile - 1.5*iqr <= num <= upper_quartile + 1.5*iqr]
    
    # Calculate the maximum, minimum, and average of the remaining numbers
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    
    return maximum, minimum, average