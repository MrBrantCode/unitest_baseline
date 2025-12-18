"""
QUESTION:
Write a function named `squared_multiplied_sum` that takes a list of integers as input, squares each element, multiplies it by 2, and returns the sum of these values. The function should check if the final sum is greater than a given threshold.
"""

def squared_multiplied_sum(numbers, threshold):
    """
    This function squares each element in the input list, multiplies it by 2, 
    and returns the sum of these values. It also checks if the final sum is 
    greater than a given threshold.

    Args:
        numbers (list): A list of integers.
        threshold (int): The threshold to compare the final sum with.

    Returns:
        int: The sum of squared and multiplied elements.
    """

    sum_squared_multiplied = sum(num**2 * 2 for num in numbers)
    
    if sum_squared_multiplied > threshold:
        print("The final sum is greater than the threshold.")
    else:
        print("The final sum is not greater than the threshold.")
    
    return sum_squared_multiplied