"""
QUESTION:
Create a function named `calculate_average` that takes a list of elements as input, calculates the average of the numeric values, and returns the result as a string rounded to two decimal places. The function should handle empty lists by returning "Error: Empty list", skip non-numeric elements, and handle cases where no valid numbers are present by returning "Error: No valid numbers found".
"""

def calculate_average(numbers):
    """
    Calculate the average of numeric values in a list.

    Args:
        numbers (list): A list of elements that may contain numeric values.

    Returns:
        str: The average of the numeric values rounded to two decimal places as a string.
             Returns "Error: Empty list" if the input list is empty.
             Returns "Error: No valid numbers found" if the list does not contain any numeric values.
    """
    if not numbers:  
        return "Error: Empty list"
    
    sum = 0
    count = 0
    
    for num in numbers:
        if isinstance(num, (int, float)):  
            sum += num
            count += 1
    
    if count == 0:  
        return "Error: No valid numbers found"
    
    average = round(sum / count, 2)  
    
    return f"The average is: {average}"