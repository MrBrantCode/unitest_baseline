"""
QUESTION:
Write a function called `calculate_odd_average` that takes a list of integers as input and returns the average of all odd elements in the list. The function should not use any built-in functions to calculate the sum or average of elements, nor should it use the modulus operator to check if a number is odd. If the list does not contain any odd numbers, the function should return a message indicating this. The time complexity of the function should be O(n), where n is the size of the list. The function should not use any additional data structures to store intermediate results, and it should not use the `len()` function to determine the size of the list.
"""

def calculate_odd_average(lst):
    """
    This function calculates the average of all odd elements in a list of integers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        float: The average of all odd elements in the list, or a message if the list does not contain any odd numbers.
    """
    odd_sum = 0
    odd_count = 0
    
    for num in lst:
        # Check if the number is odd using bitwise AND operation
        if num & 1 == 1:
            odd_sum += num
            odd_count += 1
    
    if odd_count > 0:
        # Calculate the average by dividing the sum by the count
        return odd_sum / odd_count
    else:
        # Return a message if the list does not contain any odd numbers
        return "The list does not contain any odd numbers."