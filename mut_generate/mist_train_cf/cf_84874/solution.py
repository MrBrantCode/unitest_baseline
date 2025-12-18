"""
QUESTION:
Create a function `median` that computes the median of a list of numbers. The function should accept a list of numbers with a length between 5 and 20 (inclusive), and return the median of the numbers. The function should handle both cases where the length of the list is even or odd. If the list length is not within the specified range, the function should return an error message.
"""

def median(numbers):
    """Compute the median of a list of numbers"""
    n_num = len(numbers)
    
    if n_num < 5 or n_num > 20:
        return "Invalid number of elements. Please input between 5 to 20 numbers."
        
    numbers = sorted(numbers)

    if n_num % 2 == 0:
        median1 = numbers[n_num//2]
        median2 = numbers[n_num//2 - 1]
        median = (median1 + median2)/2
    else:
        median = numbers[n_num//2]
        
    return median